from pathlib import Path

from semantics.linters.rules import lint_registry, load_lint_config
from semantics.validators.validate import validate_path


def test_valid_fixture_has_no_lint_errors():
    diagnostics, registry = validate_path(Path("tests/fixtures/valid"))
    assert diagnostics == []

    lint_diagnostics = lint_registry(registry)

    assert not any(d.severity == "error" for d in lint_diagnostics)


def test_lint_config_can_disable_rule(tmp_path: Path):
    manifest = tmp_path / "semantics.yaml"
    manifest.write_text(
        """
id: test-package
kind: semantic_package
name: Test Package
display_name: Test Package
description: Test package for lint configuration.
owner: Data Governance
version: 0.2.0
spec_version: 0.2.0
lint:
  rules:
    SAC-LINT-005: off
extensions: {}
""",
        encoding="utf-8",
    )

    config = load_lint_config(tmp_path)

    assert config["SAC-LINT-005"] == "off"
