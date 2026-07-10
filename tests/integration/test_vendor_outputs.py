from pathlib import Path

import json
import yaml

from semantics.generators.dbt import generate_dbt
from semantics.generators.openmetadata import generate_openmetadata
from semantics.validators.validate import validate_path


def test_dbt_generator_output_contains_metrics_and_semantic_models(tmp_path: Path):
    diagnostics, registry = validate_path(Path("examples/supply-chain"))
    assert diagnostics == []

    generate_dbt(registry, tmp_path)
    payload = yaml.safe_load((tmp_path / "semantic_models.yml").read_text(encoding="utf-8"))

    assert payload["semantic_models"]
    assert any(metric["name"] == "revenue" for metric in payload["metrics"])


def test_openmetadata_generator_output_contains_glossary_and_domains(tmp_path: Path):
    diagnostics, registry = validate_path(Path("examples/supply-chain"))
    assert diagnostics == []

    generate_openmetadata(registry, tmp_path)
    payload = json.loads((tmp_path / "openmetadata.json").read_text(encoding="utf-8"))

    assert payload["glossary"]
    assert any(domain["name"] == "Finance" for domain in payload["domains"])
