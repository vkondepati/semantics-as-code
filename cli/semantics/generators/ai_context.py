import json
from pathlib import Path
from typing import Any, Dict, List

from semantics.core.registry import Registry, SemanticObject


def generate_ai_context(registry: Registry, output_path: Path) -> List[Path]:
    output_path.mkdir(parents=True, exist_ok=True)
    objects = [_context_object(obj) for obj in registry.all() if obj.kind in {"entity", "metric", "glossary_term"}]
    json_path = output_path / "ai-context.json"
    md_path = output_path / "ai-context.md"
    json_path.write_text(json.dumps({"semantic_context": objects}, indent=2), encoding="utf-8")
    md_path.write_text(_markdown(objects), encoding="utf-8")
    return [json_path, md_path]


def _context_object(obj: SemanticObject) -> Dict[str, Any]:
    data = obj.data
    return {
        "id": obj.id,
        "kind": obj.kind,
        "name": obj.name,
        "description": data.get("description") or data.get("definition", ""),
        "domain": data.get("domain"),
        "owner": data.get("owner"),
        "synonyms": data.get("synonyms", []),
        "ai_context": data.get("ai_context"),
        "relationships": data.get("relationships", []),
        "dimensions": data.get("dimensions", []),
    }


def _markdown(objects: List[Dict[str, Any]]) -> str:
    lines = ["# AI Context", ""]
    for obj in objects:
        lines.extend(
            [
                f"## {obj['name']}",
                "",
                f"- ID: `{obj['id']}`",
                f"- Kind: `{obj['kind']}`",
                f"- Domain: {obj.get('domain') or 'Not specified'}",
                "",
                str(obj.get("ai_context") or obj.get("description") or ""),
                "",
            ]
        )
    return "\n".join(lines)
