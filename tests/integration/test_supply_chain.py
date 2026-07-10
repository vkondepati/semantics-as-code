from pathlib import Path

from semantics.generators.registry import GENERATORS
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


def test_all_generators_create_expected_files(tmp_path: Path):
    diagnostics, registry = validate_path(Path("examples/supply-chain"))
    assert diagnostics == []

    generated_names = {}
    for target, generator in GENERATORS.items():
        if target == "ai_context":
            continue
        output_path = tmp_path / target
        generated = generator(registry, output_path)
        generated_names[target] = {path.name for path in generated}

    assert {"index.md", "domains.md", "entities.md", "metrics.md", "glossary.md", "relationships.md"} <= generated_names["markdown"]
    assert "semantic-graph.mmd" in generated_names["mermaid"]
    assert "index.html" in generated_names["html"]
    assert "semantic_models.yml" in generated_names["dbt"]
    assert "openmetadata.json" in generated_names["openmetadata"]
    assert {"ai-context.json", "ai-context.md"} <= generated_names["ai-context"]
    assert "Customer" in (tmp_path / "markdown" / "entities.md").read_text(encoding="utf-8")
    assert "Revenue" in (tmp_path / "markdown" / "metrics.md").read_text(encoding="utf-8")


def test_retail_example_validates_and_lints_cleanly():
    diagnostics, registry = validate_path(Path("examples/retail"))

    assert diagnostics == []
    lint_diagnostics = lint_registry(registry)
    assert not any(d.severity == "error" for d in lint_diagnostics)
    assert len(registry.by_kind("entity")) >= 5
    assert len(registry.by_kind("metric")) >= 3
