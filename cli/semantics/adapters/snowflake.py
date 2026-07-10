from pathlib import Path
from typing import List

from semantics.adapters.base import VendorAdapter
from semantics.adapters.common import entity_payloads, metric_payloads, write_yaml
from semantics.core.registry import Registry


class SnowflakeAdapter(VendorAdapter):
    name = "snowflake"

    def generate(self, registry: Registry, output_path: Path) -> List[Path]:
        payload = {"semantic_model": {"tables": entity_payloads(registry), "metrics": metric_payloads(registry)}}
        return [write_yaml(output_path / "snowflake_semantic_model.yml", payload)]
