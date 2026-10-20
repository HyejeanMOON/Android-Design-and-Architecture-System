#!/usr/bin/env python3
"""Build a skills-only Codex plugin ZIP from the repository source."""

import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
SKILL = Path("skills/android-architecture-design")
MANIFESTS = (Path("plugin.json"), Path(".codex-plugin/plugin.json"))


def package(output: Path, root: Path = ROOT) -> list[Path]:
    root = root.resolve()
    portable = json.loads((root / MANIFESTS[0]).read_text(encoding="utf-8"))
    compatible = json.loads((root / MANIFESTS[1]).read_text(encoding="utf-8"))
    if any(portable.get(key) != compatible.get(key) for key in ("name", "version", "description")):
        raise ValueError("plugin manifests disagree on identity")
    if not (root / SKILL / "SKILL.md").is_file():
        raise ValueError("skill entry is missing")

    paths = [
        *MANIFESTS,
        SKILL / "SKILL.md",
        SKILL / "agents/openai.yaml",
        *(path.relative_to(root) for path in (root / SKILL / "references").glob("*.md")),
    ]
    paths = sorted(paths)
    for path in paths:
        source = root / path
        if not source.is_file() or source.is_symlink() or not source.resolve().is_relative_to(root):
            raise ValueError(f"unsafe package path: {path}")

    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for path in paths:
            archive.write(root / path, arcname=path.as_posix())
    with ZipFile(output) as archive:
        if archive.testzip() is not None:
            raise ValueError("ZIP integrity check failed")
        if set(archive.namelist()) != {path.as_posix() for path in paths}:
            raise ValueError("ZIP contents differ from the package file list")
    return paths


def main() -> None:
    version = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))["version"]
    output = ROOT / "dist" / f"android-architecture-design-{version}.zip"
    paths = package(output)
    print(f"Created {output} with {len(paths)} files")


if __name__ == "__main__":
    main()
