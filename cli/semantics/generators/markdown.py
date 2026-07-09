from pathlib import Path
from typing import List

from semantics.core.registry import Registry, SemanticObject


def generate_markdown(registry: Registry, output_path: Path) -> List[Path]:
    output_path.mkdir(parents=True, exist_ok=True)
    generated = [
        _write(output_path / "index.md", _index(registry)),
        _write(output_path / "domains.md", _objects_page("Domains", registry.by_kind("domain"))),
        _write(output_path / "entities.md", _objects_page("Entities", registry.by_kind("entity"))),
        _write(output_path / "metrics.md", _objects_page("Metrics", registry.by_kind("metric"))),
        _write(output_path / "glossary.md", _objects_page("Glossary", registry.by_kind("glossary_term"))),
        _write(output_path / "relationships.md", _objects_page("Relationships", registry.by_kind("relationship"))),
    ]
    return generated


def _write(path: Path, content: str) -> Path:
    path.write_text(content, encoding="utf-8")
    return path


def _index(registry: Registry) -> str:
    counts = {
        "Domains": len(registry.by_kind("domain")),
        "Entities": len(registry.by_kind("entity")),
        "Metrics": len(registry.by_kind("metric")),
        "Glossary Terms": len(registry.by_kind("glossary_term")),
        "Relationships": len(registry.by_kind("relationship")),
        "Quality Expectations": len(registry.by_kind("quality_expectation")),
    }
    lines = ["# Semantic Package", "", "## Summary", ""]
    lines.extend([f"- {name}: {count}" for name, count in counts.items()])
    lines.extend(
        [
            "",
            "## Pages",
            "",
            "- [Domains](domains.md)",
            "- [Entities](entities.md)",
            "- [Metrics](metrics.md)",
            "- [Glossary](glossary.md)",
            "- [Relationships](relationships.md)",
            "",
        ]
    )
    return "\n".join(lines)


def _objects_page(title: str, objects: List[SemanticObject]) -> str:
    lines = [f"# {title}", ""]
    if not objects:
        lines.append("No objects defined.")
        lines.append("")
        return "\n".join(lines)

    for obj in objects:
        lines.extend(_object_section(obj))
    return "\n".join(lines)


def _object_section(obj: SemanticObject) -> List[str]:
    data = obj.data
    description = data.get("description") or data.get("definition") or ""
    lines = [
        f"## {data.get('display_name', obj.name)}",
        "",
        description,
        "",
        f"- ID: `{obj.id}`",
        f"- Kind: `{obj.kind}`",
        f"- Owner: {data.get('owner', 'Not specified')}",
    ]
    if data.get("steward"):
        lines.append(f"- Steward: {data['steward']}")
    if data.get("domain"):
        lines.append(f"- Domain: {data['domain']}")
    if data.get("classification"):
        lines.append(f"- Classification: {data['classification']}")
    if data.get("pii") is not None:
        lines.append(f"- PII: {data['pii']}")
    if data.get("source"):
        lines.append(f"- Source: {data['source']}")
    if data.get("canonical_table"):
        lines.append(f"- Canonical table: `{data['canonical_table']}`")
    lines.append(f"- Source file: `{obj.path}`")
    lines.append("")

    for label, field in (
        ("Business Key", "business_key"),
        ("Formula", "formula"),
        ("Grain", "grain"),
        ("Relationship Type", "relationship_type"),
        ("From", "from"),
        ("To", "to"),
        ("Target", "target"),
        ("Expectation", "expectation"),
        ("Severity", "severity"),
        ("AI Context", "ai_context"),
        ("Knowledge Graph", "knowledge_graph"),
    ):
        if data.get(field):
            lines.extend([f"**{label}:** {data[field]}", ""])

    for label, field in (
        ("Dimensions", "dimensions"),
        ("Filters", "filters"),
        ("Relationships", "relationships"),
        ("Synonyms", "synonyms"),
        ("Business Rules", "business_rules"),
        ("Quality", "quality"),
        ("Glossary Terms", "glossary_terms"),
        ("Tags", "tags"),
    ):
        values = data.get(field)
        if values:
            lines.append(f"**{label}:**")
            lines.append("")
            if isinstance(values, list):
                lines.extend([f"- {value}" for value in values])
            else:
                lines.append(f"- {values}")
            lines.append("")

    return lines
