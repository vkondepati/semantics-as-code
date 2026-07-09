from pathlib import Path

from semantics.validators.validate import validate_path


def test_valid_fixture_passes_validation():
    diagnostics, registry = validate_path(Path("tests/fixtures/valid"))

    assert diagnostics == []
    assert len(list(registry.all())) == 3


def test_missing_required_field_fails_schema_validation():
    diagnostics, _registry = validate_path(Path("tests/fixtures/invalid/missing-required.yaml"))

    assert any(d.rule_id == "SAC-SCHEMA-002" for d in diagnostics)


def test_broken_reference_fails_semantic_validation():
    diagnostics, _registry = validate_path(Path("tests/fixtures/invalid/broken-reference"))

    assert any(d.rule_id == "SAC-REF-002" for d in diagnostics)
