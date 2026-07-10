import json
from pathlib import Path
from typing import Any, Dict, List

from semantics.core.registry import Registry


def generate_knowledge_graph(registry: Registry, output_path: Path) -> List[Path]:
    output_path.mkdir(parents=True, exist_ok=True)
    graph = {
        "@context": {
            "sac": "https://semantics-as-code.org/ontology/",
            "name": "sac:name",
            "kind": "sac:kind",
            "domain": "sac:domain",
            "owner": "sac:owner",
            "relatedTo": "sac:relatedTo"
        },
        "@graph": [_node(obj) for obj in registry.all() if obj.kind != "semantic_package"],
    }
    jsonld_path = output_path / "knowledge-graph.jsonld"
    ttl_path = output_path / "knowledge-graph.ttl"
    jsonld_path.write_text(json.dumps(graph, indent=2), encoding="utf-8")
    ttl_path.write_text(_ttl(registry), encoding="utf-8")
    return [jsonld_path, ttl_path]


def _node(obj) -> Dict[str, Any]:
    data = obj.data
    node = {
        "@id": f"sac:{obj.kind}/{obj.id}",
        "kind": obj.kind,
        "name": obj.name,
        "domain": data.get("domain"),
        "owner": data.get("owner"),
        "description": data.get("description") or data.get("definition", ""),
    }
    related = data.get("relationships") or data.get("dimensions") or []
    if related:
        node["relatedTo"] = related
    return node


def _ttl(registry: Registry) -> str:
    lines = [
        "@prefix sac: <https://semantics-as-code.org/ontology/> .",
        "",
    ]
    for obj in registry.all():
        if obj.kind == "semantic_package":
            continue
        subject = f"sac:{obj.kind}_{obj.id.replace('-', '_')}"
        lines.append(f"{subject} sac:kind \"{obj.kind}\" ;")
        lines.append(f"  sac:name \"{obj.name}\" .")
    return "\n".join(lines) + "\n"
