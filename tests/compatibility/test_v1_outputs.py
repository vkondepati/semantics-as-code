from pathlib import Path

from semantics.generators.registry import GENERATORS
from semantics.validators.validate import validate_path


def test_v1_generator_compatibility_surface(tmp_path: Path):
    diagnostics, registry = validate_path(Path("examples/supply-chain"))
    assert diagnostics == []

    targets = {
        "markdown": "index.md",
        "mermaid": "semantic-graph.mmd",
        "html": "index.html",
        "dbt": "semantic_models.yml",
        "openmetadata": "openmetadata.json",
        "ai-context": "ai-context.json",
        "knowledge-graph": "knowledge-graph.jsonld",
        "databricks": "databricks_metric_views.yml",
        "snowflake": "snowflake_semantic_model.yml",
        "fabric": "fabric_semantic_model.yml",
        "bigquery": "bigquery_dataform_semantics.yml",
        "openmetadata-adapter": "openmetadata.json",
        "apache-metadata": "apache_metadata_mappings.yml",
    }

    for target, expected_file in targets.items():
        generated = GENERATORS[target](registry, tmp_path / target)
        assert expected_file in {path.name for path in generated}
