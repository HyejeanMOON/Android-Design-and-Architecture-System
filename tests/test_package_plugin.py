"""Check that the distributable ZIP contains only its runtime plugin files."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("package_plugin", ROOT / "scripts/package_plugin.py")
PACKAGE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACKAGE)


class PackagePluginTests(unittest.TestCase):
    def test_repo_marketplace_exposes_plugin_root(self):
        marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
        entry, = marketplace["plugins"]
        manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(entry["name"], manifest["name"])
        self.assertEqual(entry["source"], {"source": "local", "path": "./"})
        self.assertEqual(entry["policy"]["installation"], "AVAILABLE")

    def test_archive_contains_runtime_files_with_original_contents(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "plugin.zip"
            paths = PACKAGE.package(output, ROOT)
            with ZipFile(output) as archive:
                self.assertEqual(set(archive.namelist()), {path.as_posix() for path in paths})
                for path in paths:
                    self.assertEqual(archive.read(path.as_posix()), (ROOT / path).read_bytes())
                self.assertIn("plugin.json", archive.namelist())
                self.assertIn(".codex-plugin/plugin.json", archive.namelist())
                self.assertIn("skills/android-architecture-design/SKILL.md", archive.namelist())
                self.assertNotIn("evals/oracle.json", archive.namelist())
                self.assertNotIn("AGENTS.md", archive.namelist())


if __name__ == "__main__":
    unittest.main()
