from pathlib import Path
from typing import List

from semantics.adapters.base import VendorAdapter
from semantics.adapters.common import entity_payloads, write_yaml
from semantics.core.registry import Registry


class ApacheMetadataAdapter(VendorAdapter):
    name = "apache-metadata"

    def generate(self, registry: Registry, output_path: Path) -> List[Path]:
        payload = {
            "iceberg": {"tables": entity_payloads(registry)},
            "polaris": {"catalog_assets": entity_payloads(registry)},
            "gravitino": {"metalake_assets": entity_payloads(registry)},
        }
        return [write_yaml(output_path / "apache_metadata_mappings.yml", payload)]
