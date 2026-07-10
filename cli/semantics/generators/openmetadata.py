import json
from pathlib import Path
from typing import Any, Dict, List

from semantics.core.registry import Registry, SemanticObject


def generate_openmetadata(registry: Registry, output_path: Path) -> List[Path]:
    output_path.mkdir(parents=True, exist_ok=True)
    payload = {
        "glossary": _objects(registry.by_kind("glossary_term")),
        "domains": _objects(registry.by_kind("domain")),
        "entities": _objects(registry.by_kind("entity")),
        "metrics": _objects(registry.by_kind("metric")),
        "relationships": _objects(registry.by_kind("relationship")),
    }
    path = output_path / "openmetadata.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return [path]


def _objects(objects: List[SemanticObject]) -> List[Dict[str, Any]]:
    return [
        {
            "name": obj.name,
            "displayName": obj.data.get("display_name", obj.name),
            "description": obj.data.get("description") or obj.data.get("definition", ""),
            "owner": obj.data.get("owner"),
            "domain": obj.data.get("domain"),
            "tags": obj.data.get("tags", []),
            "sourceFile": str(obj.path),
            "extensions": obj.data.get("extensions", {}),
        }
        for obj in objects
    ]
