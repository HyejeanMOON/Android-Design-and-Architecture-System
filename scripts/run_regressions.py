#!/usr/bin/env python3
"""Compile and run deterministic Kotlin state regressions; no Android/device/model eval."""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str], environment: dict[str, str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        command, env=environment, cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kotlinc", default=shutil.which("kotlinc"))
    parser.add_argument("--java", default=shutil.which("java"))
    parser.add_argument("--candidate", type=Path, help="test an isolated repaired SearchModel.kt; all scenarios must pass")
    args = parser.parse_args()
    if not args.kotlinc or not args.java:
        print("NOT RUN: provide --kotlinc and --java or put them on PATH", file=sys.stderr)
        return 2
    environment = os.environ.copy()
    java = Path(args.java).resolve()
    # A selected JDK binary also selects the compiler launcher's JDK.
    if java.parent.name == "bin" and (java.parent.parent / "release").is_file():
        environment["JAVA_HOME"] = str(java.parent.parent)
    scenarios = {
        "latest-response-wins", "old-failure-does-not-stop-current-request",
        "session-switch-isolates-response", "same-query-has-distinct-request-identity",
        "refresh-failure-keeps-content", "ordinary-success-and-error-recovery",
    }
    expected_failures = scenarios - {"ordinary-success-and-error-recovery"}
    try:
        for xml in sorted((ROOT / "evals/cases/xml").rglob("*.xml")):
            ET.parse(xml)
        print("PASS: XML fixture well-formedness (not Android resource compilation)")
        with tempfile.TemporaryDirectory(prefix="android-state-regression-") as temporary:
            variants = [("candidate", args.candidate.resolve())] if args.candidate else [
                (variant, ROOT / f"evals/cases/state/{variant}/SearchModel.kt")
                for variant in ("input", "fixed")
            ]
            for variant, source in variants:
                jar = Path(temporary) / f"{variant}.jar"
                compiled = run([
                    args.kotlinc,
                    str(source),
                    str(ROOT / "evals/cases/state/Checks.kt"),
                    "-include-runtime", "-d", str(jar),
                ], environment)
                if compiled.returncode != 0:
                    print(f"FAIL: {variant} did not compile\n{compiled.stdout}", file=sys.stderr)
                    return 1
                result = run([args.java, "-jar", str(jar)], environment)
                passed, failed = set(), set()
                for line in result.stdout.splitlines():
                    if line.startswith("PASS "):
                        passed.add(line[5:])
                    elif line.startswith("FAIL "):
                        failed.add(line[5:].split(":", 1)[0])
                if variant == "input":
                    correct = result.returncode != 0 and failed == expected_failures and passed == scenarios - failed
                else:
                    correct = result.returncode == 0 and passed == scenarios and not failed
                if not correct:
                    print(f"FAIL: unexpected {variant} outcomes\n{result.stdout}", file=sys.stderr)
                    return 1
                print(f"PASS: {variant}: {len(passed)} passed, {len(failed)} expected failures")
    except (OSError, subprocess.TimeoutExpired, ET.ParseError) as exc:
        print(f"NOT VERIFIED: {exc}", file=sys.stderr)
        return 1
    print("Not evaluated: Android compilation, UI/lifecycle/leak runtime, independent model behavior")
    return 0


if __name__ == "__main__":
    sys.exit(main())
