from pathlib import Path
from typing import List

import yaml

from semantics.core.registry import Registry


def write_yaml(path: Path, payload) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=False), encoding="utf-8")
    return path


def metric_payloads(registry: Registry) -> List[dict]:
    return [
        {
            "name": metric.name,
            "id": metric.id,
            "description": metric.data.get("description", ""),
            "formula": metric.data.get("formula"),
            "grain": metric.data.get("grain"),
            "dimensions": metric.data.get("dimensions", []),
            "filters": metric.data.get("filters", []),
            "owner": metric.data.get("owner"),
        }
        for metric in registry.by_kind("metric")
    ]


def entity_payloads(registry: Registry) -> List[dict]:
    return [
        {
            "name": entity.name,
            "id": entity.id,
            "description": entity.data.get("description", ""),
            "business_key": entity.data.get("business_key"),
            "canonical_table": entity.data.get("canonical_table"),
            "domain": entity.data.get("domain"),
            "owner": entity.data.get("owner"),
        }
        for entity in registry.by_kind("entity")
    ]
