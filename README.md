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
semantics generate examples/supply-chain --target mermaid --output dist/diagrams
semantics generate examples/supply-chain --target html --output dist/html
```

## Website

The public documentation website lives under `website/` and is configured for GitHub Pages at:

```text
https://vkondepati.github.io/semantics-as-code/
```

Local development:

```bash
cd website
npm install
npm run dev
npm run build
npm run preview
```

To enable GitHub Pages, open repository **Settings > Pages**, set **Source** to **GitHub Actions**, then push to `main`. The `.github/workflows/deploy-website.yml` workflow builds and deploys the Astro site.

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
semantics generate <path> --target mermaid --output dist/diagrams
semantics generate <path> --target html --output dist/html
semantics generate <path> --target dbt --output dist/dbt
semantics generate <path> --target openmetadata --output dist/openmetadata
semantics generate <path> --target ai-context --output dist/ai
semantics generate <path> --target knowledge-graph --output dist/kg
semantics generate <path> --target databricks --output dist/databricks
semantics generate <path> --target snowflake --output dist/snowflake
semantics generate <path> --target fabric --output dist/fabric
semantics generate <path> --target bigquery --output dist/bigquery
semantics generate <path> --target apache-metadata --output dist/apache
semantics diff --base examples/supply-chain --head examples/retail
```

Planned commands:

```bash
semantics test <path>
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
- Version 0.2: Mermaid, HTML, dbt, OpenMetadata, AI context generators, manifests, configurable linting, semantic diff, expanded examples.
- Version 0.5: knowledge graph generation, package dependencies, formula validation, integration tests, VS Code prototype.
- Version 1.0: stable versioning policy, vendor adapter API, built-in adapters, compatibility test suite, formal specification.

## License

MIT
