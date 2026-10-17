import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "validate_plugin", Path(__file__).resolve().parents[1] / "scripts/validate_plugin.py",
)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "package"
        self.root.mkdir()
        (self.root / ".codex-plugin").mkdir()
        self.skill = self.root / "skills/android-architecture-design"
        (self.skill / "references").mkdir(parents=True)
        identity = {"name": "android-architecture-design", "version": "0.5.0", "description": "Fixture"}
        portable = {"$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", **identity}
        (self.root / "plugin.json").write_text(json.dumps(portable))
        (self.root / ".codex-plugin/plugin.json").write_text(json.dumps({**identity, "skills": "./skills/"}))
        self.entry = self.skill / "SKILL.md"
        self.entry.write_text("---\nname: android-architecture-design\ndescription: Fixture\n---\n")

    def assert_error(self, expected):
        self.assertTrue(any(expected in error for error in VALIDATOR.validate(self.root)))

    def test_self_contained_reference_is_discoverable(self):
        reference = self.skill / "references/rule.md"
        reference.write_text("Rule")
        self.entry.write_text(self.entry.read_text() + "[Rule](references/rule.md)\n")
        self.assertEqual([], VALIDATOR.validate(self.root))

    def test_malformed_manifest(self):
        (self.root / "plugin.json").write_text("{invalid")
        self.assert_error("plugin.json:")

    def test_nonobject_manifest(self):
        (self.root / "plugin.json").write_text("[]")
        self.assert_error("JSON object")

    def test_mismatched_identity(self):
        path = self.root / ".codex-plugin/plugin.json"
        manifest = json.loads(path.read_text())
        manifest["version"] = "0.4.0"
        path.write_text(json.dumps(manifest))
        self.assert_error("identity differs")

    def test_missing_skill(self):
        self.entry.unlink()
        self.assert_error("entry is missing")

    def test_invalid_frontmatter(self):
        self.entry.write_text("# No frontmatter")
        self.assert_error("frontmatter is missing")

    def test_missing_reference(self):
        self.entry.write_text(self.entry.read_text() + "[Missing](references/absent.md)\n")
        self.assert_error("missing local link")

    def test_reference_escaping_package(self):
        outside = self.root.parent / "outside.md"
        outside.write_text("outside")
        self.entry.write_text(self.entry.read_text() + "[Outside](../../../outside.md)\n")
        self.assert_error("escapes package")

    def test_skill_cannot_depend_on_author_docs(self):
        (self.root / "README.md").write_text("Author documentation")
        self.entry.write_text(self.entry.read_text() + "[Readme](../../README.md)\n")
        self.assert_error("not self-contained")

    def test_orphan_runtime_reference(self):
        (self.skill / "references/orphan.md").write_text("Not linked from entry")
        self.assert_error("not reachable")

    def test_malformed_url_reports_error_instead_of_crashing(self):
        self.entry.write_text(self.entry.read_text() + "[Broken](https://[broken)\n")
        self.assert_error("malformed URL")


if __name__ == "__main__":
    unittest.main()
