from pathlib import Path
from typing import List

import yaml

from semantics.core.registry import Registry


def generate_dbt(registry: Registry, output_path: Path) -> List[Path]:
    output_path.mkdir(parents=True, exist_ok=True)
    semantic_models = []
    metrics = []

    for entity in registry.by_kind("entity"):
        semantic_models.append(
            {
                "name": _slug(entity.name),
                "description": entity.data.get("description", ""),
                "model": f"ref('{_slug(entity.name)}')",
                "entities": [
                    {
                        "name": _slug(entity.name),
                        "type": "primary",
                        "expr": entity.data.get("business_key"),
                    }
                ],
            }
        )

    for metric in registry.by_kind("metric"):
        metrics.append(
            {
                "name": _slug(metric.name),
                "description": metric.data.get("description", ""),
                "type": "simple",
                "label": metric.data.get("display_name", metric.name),
                "type_params": {
                    "measure": {
                        "name": _slug(metric.name),
                        "expr": metric.data.get("formula"),
                    }
                },
                "filter": "; ".join(metric.data.get("filters", [])),
            }
        )

    path = output_path / "semantic_models.yml"
    path.write_text(
        yaml.safe_dump(
            {"semantic_models": semantic_models, "metrics": metrics},
            sort_keys=False,
            allow_unicode=False,
        ),
        encoding="utf-8",
    )
    return [path]


def _slug(value: str) -> str:
    return value.strip().lower().replace(" ", "_").replace("-", "_")
