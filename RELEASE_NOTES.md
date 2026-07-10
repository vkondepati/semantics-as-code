# Release Notes

## v1.0.0 - Stable Specification and Vendor Adapter Surface

### Added

- Knowledge graph generator with JSON-LD and Turtle outputs.
- Local semantic package dependency support through `semantics.yaml`.
- Richer metric formula validation for unsafe tokens, unsupported characters, and unbalanced parentheses.
- VS Code extension prototype with snippets and language configuration.
- Formal specification and specification versioning policy.
- Vendor adapter API.
- Built-in adapters for Databricks, Snowflake, Microsoft Fabric, BigQuery, OpenMetadata, and Apache Iceberg/Polaris/Gravitino mappings.
- Compatibility test suite for stable generator and adapter outputs.
- dbt and OpenMetadata integration tests.

## v0.2.0 - Generators, Manifests, Configurable Linting, and Diff

### Added

- Mermaid diagram generator with `semantic-graph.mmd` output.
- Standalone HTML documentation generator.
- dbt Semantic Layer scaffold generator with `semantic_models.yml` output.
- OpenMetadata-oriented JSON generator.
- AI context generator with Markdown and JSON outputs.
- Semantic package manifest support through root `semantics.yaml` files.
- Configurable lint rule severities through package manifests.
- Path-based `semantics diff --base <path> --head <path>`.
- Retail industry starter example.
- Tests for generators, lint configuration, retail validation, and diff.
- CI checks for retail validation and all Version 0.2 generator targets.

### Verified

- `python -m pytest`
- `python -m semantics validate examples/supply-chain`
- `python -m semantics validate examples/retail`
- `python -m semantics lint examples/supply-chain`
- `python -m semantics lint examples/retail`
- `python -m semantics generate examples/supply-chain --target mermaid --output dist/diagrams`
- `python -m semantics generate examples/supply-chain --target html --output dist/html`
- `python -m semantics generate examples/supply-chain --target dbt --output dist/dbt`
- `python -m semantics generate examples/supply-chain --target openmetadata --output dist/openmetadata`
- `python -m semantics generate examples/supply-chain --target ai-context --output dist/ai`
- `python -m semantics diff --base examples/supply-chain --head examples/retail`

## v0.1.0 - Initial Semantics as Code Starter Kit

This release establishes the first usable Semantics as Code reference implementation.

### Added

- Project README with positioning, quick start, roadmap, and comparison matrix.
- Product, design, task, specification, CLI, generator, and example documentation.
- JSON Schemas for domains, entities, metrics, glossary terms, relationships, quality expectations, and common semantic object fields.
- YAML templates for all Version 0.1 semantic object types.
- Supply chain example package with domains, entities, metrics, glossary terms, relationships, quality expectations, governance metadata, and AI context.
- Python reference CLI with:
  - `semantics validate`
  - `semantics lint`
  - `semantics generate --target markdown`
  - planned placeholders for `semantics test` and `semantics diff`
- Registry loader for recursive YAML discovery, object normalization, duplicate detection, and reference resolution.
- JSON Schema validation and semantic cross-reference validation.
- Lint rules for descriptions, ownership, stewardship, quality expectations, AI context, and naming consistency.
- Markdown documentation generator.
- Unit and integration tests.
- GitHub Actions workflow for validation, linting, tests, and documentation generation.
- Contribution guide, code of conduct, and `.gitignore`.

### Verified

- `python -m pytest`
- `python -m semantics validate examples/supply-chain`
- `python -m semantics lint examples/supply-chain`
- `python -m semantics generate examples/supply-chain --target markdown --output dist/docs`

### Not Included

- Vendor adapters.
- Mermaid or HTML generators.
- Knowledge graph generation.
- AI context file generation.
- VS Code extension.
- Remote package dependency support.
