from pathlib import Path
from typing import List

from semantics.adapters.base import VendorAdapter
from semantics.adapters.common import entity_payloads, metric_payloads, write_yaml
from semantics.core.registry import Registry


class FabricAdapter(VendorAdapter):
    name = "fabric"

    def generate(self, registry: Registry, output_path: Path) -> List[Path]:
        payload = {"power_bi_semantic_model": {"entities": entity_payloads(registry), "measures": metric_payloads(registry)}}
        return [write_yaml(output_path / "fabric_semantic_model.yml", payload)]
