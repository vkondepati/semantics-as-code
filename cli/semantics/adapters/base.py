from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from semantics.core.registry import Registry


class VendorAdapter(ABC):
    name: str

    @abstractmethod
    def generate(self, registry: Registry, output_path: Path) -> List[Path]:
        """Generate vendor-specific artifacts."""
