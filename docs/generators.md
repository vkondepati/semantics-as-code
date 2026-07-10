# Generators

Generators transform a loaded semantic registry into output artifacts. Generators consume the registry rather than parsing YAML independently.

## Supported Generators

### Markdown

Creates:

- `index.md`
- `domains.md`
- `entities.md`
- `metrics.md`
- `glossary.md`
- `relationships.md`

### Mermaid

Creates `semantic-graph.mmd` with an entity relationship diagram.

### HTML

Creates a standalone `index.html` documentation page.

### dbt

Creates `semantic_models.yml` with dbt Semantic Layer-oriented scaffolding.

### OpenMetadata

Creates `openmetadata.json` with glossary, domain, entity, metric, and relationship payloads.

### AI Context

Creates:

- `ai-context.json`
- `ai-context.md`

### Knowledge Graph

Creates:

- `knowledge-graph.jsonld`
- `knowledge-graph.ttl`

### Vendor Adapters

The adapter targets are documented in [adapters.md](adapters.md).

## Planned Generators

- Power BI semantic model scaffolding.
- OpenAPI extensions.
