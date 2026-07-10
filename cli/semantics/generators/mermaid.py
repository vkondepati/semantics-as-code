from pathlib import Path
from typing import List

from semantics.core.registry import Registry


def generate_mermaid(registry: Registry, output_path: Path) -> List[Path]:
    output_path.mkdir(parents=True, exist_ok=True)
    lines = ["erDiagram"]

    entities = registry.by_kind("entity")
    for entity in entities:
        lines.append(f"  {_node(entity.name)} {{")
        business_key = entity.data.get("business_key", "id")
        lines.append(f"    string {business_key}")
        lines.append("  }")

    for relationship in registry.by_kind("relationship"):
        left = registry.resolve(relationship.data.get("from"))
        right = registry.resolve(relationship.data.get("to"))
        if not left or not right:
            continue
        connector = _connector(relationship.data.get("relationship_type"))
        label = relationship.data.get("display_name", relationship.name)
        lines.append(f"  {_node(left.name)} {connector} {_node(right.name)} : \"{label}\"")

    path = output_path / "semantic-graph.mmd"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return [path]


def _node(value: str) -> str:
    return value.replace(" ", "_").replace("-", "_")


def _connector(relationship_type: str) -> str:
    return {
        "one_to_one": "||--||",
        "one_to_many": "||--o{",
        "many_to_one": "}o--||",
        "many_to_many": "}o--o{",
    }.get(relationship_type, "||--o{")
