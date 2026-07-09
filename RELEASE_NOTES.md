# Release Notes

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
