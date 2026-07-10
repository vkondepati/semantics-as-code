from pathlib import Path
from typing import List

from semantics.adapters.base import VendorAdapter
from semantics.adapters.common import metric_payloads, write_yaml
from semantics.core.registry import Registry


class BigQueryAdapter(VendorAdapter):
    name = "bigquery"

    def generate(self, registry: Registry, output_path: Path) -> List[Path]:
        payload = {"dataform_semantic_assertions": metric_payloads(registry)}
        return [write_yaml(output_path / "bigquery_dataform_semantics.yml", payload)]
