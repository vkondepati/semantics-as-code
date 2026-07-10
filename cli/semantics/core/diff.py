import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

from semantics.core.errors import Diagnostic
from semantics.core.registry import Registry
from semantics.validators.validate import validate_path


@dataclass
class DiffResult:
    diagnostics: List[Diagnostic]
    added: List[str]
    removed: List[str]
    changed: List[str]

    @property
    def has_changes(self) -> bool:
        return bool(self.added or self.removed or self.changed)


def diff_paths(base: Path, head: Path) -> DiffResult:
    diagnostics: List[Diagnostic] = []
    base_diagnostics, base_registry = validate_path(base)
    head_diagnostics, head_registry = validate_path(head)
    diagnostics.extend(base_diagnostics)
    diagnostics.extend(head_diagnostics)
    if any(d.severity == "error" for d in diagnostics):
        return DiffResult(diagnostics=diagnostics, added=[], removed=[], changed=[])

    base_objects = _fingerprints(base_registry)
    head_objects = _fingerprints(head_registry)

    base_ids = set(base_objects)
    head_ids = set(head_objects)
    added = sorted(head_ids - base_ids)
    removed = sorted(base_ids - head_ids)
    changed = sorted(object_id for object_id in base_ids & head_ids if base_objects[object_id] != head_objects[object_id])
    return DiffResult(diagnostics=diagnostics, added=added, removed=removed, changed=changed)


def _fingerprints(registry: Registry) -> Dict[str, str]:
    fingerprints = {}
    for obj in registry.all():
        payload = {key: value for key, value in obj.data.items() if key != "source_file"}
        fingerprints[f"{obj.kind}:{obj.id}"] = json.dumps(payload, sort_keys=True)
    return fingerprints
