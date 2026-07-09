from pathlib import Path

from semantics.linters.rules import lint_registry
from semantics.validators.validate import validate_path


def test_valid_fixture_has_no_lint_errors():
    diagnostics, registry = validate_path(Path("tests/fixtures/valid"))
    assert diagnostics == []

    lint_diagnostics = lint_registry(registry)

    assert not any(d.severity == "error" for d in lint_diagnostics)
