from html import escape
from pathlib import Path
from typing import List

from semantics.core.registry import Registry, SemanticObject


def generate_html(registry: Registry, output_path: Path) -> List[Path]:
    output_path.mkdir(parents=True, exist_ok=True)
    path = output_path / "index.html"
    sections = [
        _section("Domains", registry.by_kind("domain")),
        _section("Entities", registry.by_kind("entity")),
        _section("Metrics", registry.by_kind("metric")),
        _section("Glossary", registry.by_kind("glossary_term")),
        _section("Relationships", registry.by_kind("relationship")),
    ]
    package = registry.package()
    title = package.data.get("display_name", "Semantic Package") if package else "Semantic Package"
    content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <style>
    body {{ font-family: Arial, sans-serif; line-height: 1.5; margin: 2rem; color: #1f2933; }}
    h1, h2, h3 {{ color: #102a43; }}
    .grid {{ display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }}
    .card {{ border: 1px solid #d9e2ec; border-radius: 8px; padding: 1rem; background: #fff; }}
    code {{ background: #f0f4f8; padding: 0.1rem 0.25rem; }}
  </style>
</head>
<body>
  <h1>{escape(title)}</h1>
  {''.join(sections)}
</body>
</html>
"""
    path.write_text(content, encoding="utf-8")
    return [path]


def _section(title: str, objects: List[SemanticObject]) -> str:
    cards = "".join(_card(obj) for obj in objects) or "<p>No objects defined.</p>"
    return f"<section><h2>{escape(title)}</h2><div class=\"grid\">{cards}</div></section>"


def _card(obj: SemanticObject) -> str:
    data = obj.data
    description = data.get("description") or data.get("definition") or ""
    meta = [
        f"<p><strong>ID:</strong> <code>{escape(obj.id)}</code></p>",
        f"<p><strong>Owner:</strong> {escape(str(data.get('owner', 'Not specified')))}</p>",
    ]
    if data.get("domain"):
        meta.append(f"<p><strong>Domain:</strong> {escape(str(data['domain']))}</p>")
    if data.get("classification"):
        meta.append(f"<p><strong>Classification:</strong> {escape(str(data['classification']))}</p>")
    return (
        "<article class=\"card\">"
        f"<h3>{escape(str(data.get('display_name', obj.name)))}</h3>"
        f"<p>{escape(str(description))}</p>"
        f"{''.join(meta)}"
        "</article>"
    )
