from pathlib import Path
from typing import List

from semantics.adapters.base import VendorAdapter
from semantics.core.registry import Registry
from semantics.generators.openmetadata import generate_openmetadata


class OpenMetadataAdapter(VendorAdapter):
    name = "openmetadata-adapter"

    def generate(self, registry: Registry, output_path: Path) -> List[Path]:
        return generate_openmetadata(registry, output_path)
