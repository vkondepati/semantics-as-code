from pathlib import Path
from typing import List

from semantics.adapters.base import VendorAdapter
from semantics.adapters.common import metric_payloads, write_yaml
from semantics.core.registry import Registry


class DatabricksAdapter(VendorAdapter):
    name = "databricks"

    def generate(self, registry: Registry, output_path: Path) -> List[Path]:
        payload = {"metric_views": metric_payloads(registry)}
        return [write_yaml(output_path / "databricks_metric_views.yml", payload)]
