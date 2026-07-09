from pathlib import Path

from semantics.generators.markdown import generate_markdown
from semantics.linters.rules import lint_registry
from semantics.validators.validate import validate_path


def test_supply_chain_example_validates_and_lints_cleanly():
    diagnostics, registry = validate_path(Path("examples/supply-chain"))

    assert diagnostics == []
    lint_diagnostics = lint_registry(registry)
    assert not any(d.severity == "error" for d in lint_diagnostics)
    assert len(registry.by_kind("domain")) >= 3
    assert len(registry.by_kind("entity")) >= 5
    assert len(registry.by_kind("metric")) >= 3


def test_markdown_generator_creates_expected_files(tmp_path: Path):
    diagnostics, registry = validate_path(Path("examples/supply-chain"))
    assert diagnostics == []

    generated = generate_markdown(registry, tmp_path)

    generated_names = {path.name for path in generated}
    assert {"index.md", "domains.md", "entities.md", "metrics.md", "glossary.md", "relationships.md"} <= generated_names
    assert "Customer" in (tmp_path / "entities.md").read_text(encoding="utf-8")
    assert "Revenue" in (tmp_path / "metrics.md").read_text(encoding="utf-8")
