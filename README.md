# Semantics as Code

Semantics as Code is an open-source, vendor-neutral specification and starter kit for defining enterprise business semantics as version-controlled, testable, deployable code.

It lets teams describe business entities, metrics, domains, glossary terms, relationships, governance metadata, quality expectations, and AI context in YAML. Those definitions can be validated in CI/CD and generated into documentation or downstream platform artifacts.

## What This Is

- An open specification for enterprise semantic modeling.
- A Git-first way to manage business meaning.
- A starter kit for business entities, metrics, glossary terms, governance, and quality rules.
- A reference CLI for validation, linting, and documentation generation.
- A foundation for future adapters to dbt, OpenMetadata, Databricks, Snowflake, Fabric, Power BI, knowledge graphs, and AI context systems.

## What This Is Not

- Not a BI tool.
- Not a metric runtime.
- Not a data catalog.
- Not a governance platform.
- Not a replacement for dbt, OpenMetadata, LookML, Cube, AtScale, Databricks, Snowflake, Fabric, or Power BI.

Think OpenAPI for business semantics: a portable specification that other tools can consume or generate.

## Quick Start

```bash
pip install -e ".[dev]"
semantics validate examples/supply-chain
semantics lint examples/supply-chain
semantics generate examples/supply-chain --target markdown --output dist/docs
```

## Repository Structure

```text
docs/                 Product, design, CLI, and specification docs
schemas/              JSON Schemas for semantic YAML objects
templates/            Starter YAML templates
examples/             Example semantic packages
cli/                  Python reference CLI
tests/                Unit and integration tests
.github/workflows/    CI validation workflow
```

## MVP Object Types

- `domain`
- `entity`
- `metric`
- `glossary_term`
- `relationship`
- `quality_expectation`

## CLI

```bash
semantics validate <path>
semantics lint <path>
semantics generate <path> --target markdown --output dist/docs
```

Planned commands:

```bash
semantics test <path>
semantics diff --base main --head current
```

## Comparison Matrix

| Capability | OpenMetadata | dbt Semantic Layer | Databricks Metric Views | Snowflake OSI | Semantics as Code |
| --- | --- | --- | --- | --- | --- |
| Business glossary | Yes | Partial | No | Partial | Yes |
| Vendor neutral | Yes | Partial | No | Yes | Yes |
| Version-controlled in Git | Partial | Yes | Partial | Partial | Yes |
| Deployable as code | Partial | Yes | Yes | Partial | Yes |
| Enterprise semantic blueprint | No | No | No | No | Yes |
| Starter templates | Limited | Limited | No | No | Yes |
| Multi-platform artifact generation | No | No | No | No | Yes |

## Roadmap

- Version 0.1: specification, starter kit, schemas, validation, linting, Markdown docs, CI.
- Version 0.2: generators, documentation site, metric view generation, expanded examples.
- Version 0.5: knowledge graph generation, AI context generation, OpenMetadata and dbt integrations.
- Version 1.0: stable vendor adapters and compatibility test suite.

## License

MIT
