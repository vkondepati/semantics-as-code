from pathlib import Path

from semantics.adapters.registry import ADAPTERS
from semantics.generators.knowledge_graph import generate_knowledge_graph
from semantics.validators.validate import validate_path


def test_vendor_adapters_generate_expected_files(tmp_path: Path):
    diagnostics, registry = validate_path(Path("examples/supply-chain"))
    assert diagnostics == []

    expected = {
        "databricks": "databricks_metric_views.yml",
        "snowflake": "snowflake_semantic_model.yml",
        "fabric": "fabric_semantic_model.yml",
        "bigquery": "bigquery_dataform_semantics.yml",
        "openmetadata-adapter": "openmetadata.json",
        "apache-metadata": "apache_metadata_mappings.yml",
    }

    for name, adapter in ADAPTERS.items():
        generated = adapter.generate(registry, tmp_path / name)
        assert expected[name] in {path.name for path in generated}


def test_knowledge_graph_generator_creates_jsonld_and_turtle(tmp_path: Path):
    diagnostics, registry = validate_path(Path("examples/supply-chain"))
    assert diagnostics == []

    generated = generate_knowledge_graph(registry, tmp_path)

    names = {path.name for path in generated}
    assert {"knowledge-graph.jsonld", "knowledge-graph.ttl"} <= names
    assert "Customer" in (tmp_path / "knowledge-graph.jsonld").read_text(encoding="utf-8")
