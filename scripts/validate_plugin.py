#!/usr/bin/env python3
"""Validate this instruction-only plugin's structure; no Android or model evaluation."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    manifests = []
    for name in ("plugin.json", ".codex-plugin/plugin.json"):
        try:
            value = json.loads((root / name).read_text(encoding="utf-8"))
            if not isinstance(value, dict):
                raise ValueError("manifest must be a JSON object")
            manifests.append(value)
        except (OSError, ValueError) as exc:
            errors.append(f"{name}: {exc}")
    if len(manifests) == 2:
        portable, legacy = manifests
        for key in ("name", "version", "description"):
            if not portable.get(key) or portable.get(key) != legacy.get(key):
                errors.append(f"manifest identity differs or is empty: {key}")
        if portable.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
            errors.append("unexpected portable manifest schema")
        if legacy.get("skills") != "./skills/":
            errors.append("compatibility skills path must be ./skills/")
        if portable.get("name") != "android-architecture-design":
            errors.append("manifest name does not match the packaged skill")
        version = portable.get("version")
        if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", version):
            errors.append("manifest version must be a three-part version")

    skill_root = root / "skills" / "android-architecture-design"
    entry = skill_root / "SKILL.md"
    if not entry.is_file():
        errors.append("skill entry is missing")
    else:
        source = entry.read_text(encoding="utf-8")
        header = re.match(r"\A---\n(.*?)\n---(?:\n|$)", source, re.S)
        if not header:
            errors.append("skill YAML frontmatter is missing")
        else:
            for field in ("name", "description"):
                if not re.search(rf"^{field}:\s*\S", header[1], re.M):
                    errors.append(f"skill frontmatter is missing {field}")
            if not re.search(r"^name: android-architecture-design$", header[1], re.M):
                errors.append("skill name does not match its directory")

    # Resolve local Markdown links only; network availability is not a packaging check.
    graph = {}
    for document in sorted(root.rglob("*.md")):
        if any(part.startswith(".") for part in document.relative_to(root).parts):
            continue
        graph[document.resolve()] = set()
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", document.read_text(encoding="utf-8")):
            try:
                url = urlsplit(target)
            except ValueError:
                errors.append(f"{document.relative_to(root)}: malformed URL: {target}")
                continue
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (document.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(root):
                errors.append(f"{document.relative_to(root)}: link escapes package: {target}")
            elif document.is_relative_to(skill_root) and not resolved.is_relative_to(skill_root):
                errors.append(f"{document.relative_to(root)}: skill link is not self-contained: {target}")
            elif not resolved.exists():
                errors.append(f"{document.relative_to(root)}: missing local link: {target}")
            else:
                graph[document.resolve()].add(resolved)
    # Discoverability is structural; links do not require recursive loading at runtime.
    reachable, pending = set(), [entry.resolve()]
    while pending:
        current = pending.pop()
        if current in reachable:
            continue
        reachable.add(current)
        pending.extend(graph.get(current, set()) - reachable)
    for reference in (skill_root / "references").rglob("*.md"):
        if reference.resolve() not in reachable:
            errors.append(f"skill reference is not reachable from SKILL.md: {reference.name}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print("Plugin structure validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PASS: manifests, skill entry, local Markdown links and reference discoverability")
    skill = root / "skills/android-architecture-design"
    documents = [skill / "SKILL.md", *(skill / "references").glob("*.md")]
    print(f"Runtime Markdown: {len(documents)} files, {sum(path.stat().st_size for path in documents)} bytes")
    print("Not evaluated: host installation, full JSON/YAML schemas, Android code or model behavior")
    return 0


if __name__ == "__main__":
    sys.exit(main())
