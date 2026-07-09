# Technical Design: Semantics as Code

## 1. Design Summary

Semantics as Code is designed as a specification-first open-source project. The core product is a set of versioned YAML schemas, validation rules, example semantic packages, and generators that transform semantic definitions into useful artifacts.

The architecture separates the stable semantic specification from optional adapters and generators. This keeps the project vendor neutral while still allowing integrations with platforms such as dbt, OpenMetadata, Databricks, Snowflake, Fabric, Power BI, and knowledge graph systems.

## 2. Design Goals

- Keep the core specification portable and independent of any runtime platform.
- Make semantic definitions easy to author, review, validate, and diff in Git.
- Provide clear extension points for industries, organizations, and vendors.
- Support both human-readable documentation and machine-consumable outputs.
- Enable a small Version 0.1 implementation that can grow without rework.

## 3. System Architecture

```text
YAML source files
      |
      v
Schema validation
      |
      v
Semantic registry loader
      |
      v
Cross-reference validation and linting
      |
      +------------------+
      |                  |
      v                  v
Generated docs      Vendor/output generators
      |                  |
      v                  v
Markdown, HTML,     dbt, OpenMetadata,
Mermaid, AI files   Power BI, graph, etc.
```

## 4. Repository Architecture

```text
semantics-as-code/
  docs/
    PRD.md
    DESIGN.md
    TASKS.md
    specification.md
    cli.md
    generators.md
  schemas/
    semantic-object.schema.json
    entity.schema.json
    metric.schema.json
    domain.schema.json
    glossary-term.schema.json
    relationship.schema.json
    quality-expectation.schema.json
  templates/
    entity.yaml
    metric.yaml
    domain.yaml
    glossary-term.yaml
    relationship.yaml
    quality-expectation.yaml
  examples/
    supply-chain/
      domains/
      entities/
      metrics/
      glossary/
      quality/
  cli/
    semantics/
      commands/
      core/
      generators/
      validators/
      linters/
  tests/
    fixtures/
    unit/
    integration/
  .github/
    workflows/
      validate.yml
```

## 5. Core Concepts

### 5.1 Semantic Package

A semantic package is a directory containing Semantics as Code YAML files. The package may represent an enterprise, a domain, a product area, or an industry starter kit.

Recommended package structure:

```text
domains/
entities/
metrics/
glossary/
relationships/
quality/
knowledge_graph/
```

### 5.2 Semantic Object

All semantic objects share a common metadata envelope.

Required common fields:

- `id`
- `kind`
- `name`
- `display_name`
- `description`
- `owner`
- `version`

Recommended common fields:

- `domain`
- `steward`
- `tags`
- `status`
- `classification`
- `source`
- `extensions`

The `extensions` field allows vendor-specific or organization-specific metadata without changing the core schema.

### 5.3 Registry

The registry is the in-memory model built by loading all YAML files in a semantic package. It is responsible for:

- Normalizing object identifiers.
- Tracking source file paths.
- Detecting duplicate identifiers.
- Resolving references.
- Providing a common input model for validators, linters, tests, and generators.

## 6. YAML Object Design

### 6.1 Entity

Entity files define business concepts such as Customer, Product, Order, Supplier, or Region.

Required fields:

- `id`
- `kind: entity`
- `name`
- `display_name`
- `description`
- `business_key`
- `owner`

Optional fields:

- `steward`
- `domain`
- `classification`
- `pii`
- `canonical_table`
- `relationships`
- `synonyms`
- `business_rules`
- `quality`
- `knowledge_graph`
- `ai_context`
- `extensions`

### 6.2 Metric

Metric files define governed calculations such as Revenue, Gross Margin, Churn Rate, or On-Time Delivery.

Required fields:

- `id`
- `kind: metric`
- `name`
- `display_name`
- `description`
- `formula`
- `grain`
- `owner`

Optional fields:

- `domain`
- `dimensions`
- `filters`
- `source`
- `quality`
- `synonyms`
- `glossary_terms`
- `ai_context`
- `extensions`

### 6.3 Domain

Domain files group semantic objects into business areas such as Sales, Finance, Supply Chain, or Manufacturing.

Required fields:

- `id`
- `kind: domain`
- `name`
- `display_name`
- `description`
- `owner`

### 6.4 Glossary Term

Glossary terms define shared business language and can map to entities, metrics, or dimensions.

Required fields:

- `id`
- `kind: glossary_term`
- `name`
- `display_name`
- `definition`
- `owner`

### 6.5 Relationship

Relationships define how semantic objects connect.

Required fields:

- `id`
- `kind: relationship`
- `from`
- `to`
- `relationship_type`
- `description`

### 6.6 Quality Expectation

Quality expectations define business-level expectations attached to entities or metrics.

Required fields:

- `id`
- `kind: quality_expectation`
- `target`
- `expectation`
- `severity`
- `owner`

## 7. Schema Strategy

Version 0.1 should use JSON Schema Draft 2020-12 for YAML validation. YAML files are parsed into JSON-compatible objects and validated against the relevant schema based on the `kind` field.

Schema design rules:

- Use strict required fields for MVP object validity.
- Allow `extensions` for safe customization.
- Keep vendor-specific fields outside the core schema.
- Include examples in each schema.
- Publish schemas in predictable paths for editor integration.

## 8. CLI Design

The CLI command should be named `semantics`.

### 8.1 Commands

```text
semantics validate [path]
semantics lint [path]
semantics test [path]
semantics generate [path] --target markdown --output dist/docs
semantics diff --base main --head current
```

### 8.2 Version 0.1 Command Scope

Version 0.1 should implement:

- `semantics validate`
- `semantics lint`
- `semantics generate --target markdown`

The `test` and `diff` commands can be documented as planned commands until their rules are fully designed.

### 8.3 Exit Codes

- `0`: success.
- `1`: validation, lint, or generation failure.
- `2`: invalid CLI arguments.
- `3`: internal error.

### 8.4 Error Format

CLI errors should include:

- File path.
- Line number when available.
- Object id when available.
- Rule id.
- Human-readable message.
- Suggested fix when possible.

Example:

```text
examples/supply-chain/entities/customer.yaml:12 [SAC-REF-001]
Relationship target "Orders" was not found.
Suggestion: define an entity with id "order" or update the relationship reference.
```

## 9. Validation Design

Validation has three layers.

### 9.1 Parse Validation

Checks that files are readable YAML.

### 9.2 Schema Validation

Checks that each object conforms to its JSON Schema.

### 9.3 Semantic Validation

Checks cross-file and project-level rules:

- Unique object ids.
- Valid domain references.
- Valid entity relationships.
- Valid metric dimensions.
- Valid glossary mappings.
- Supported classification values.
- Supported lifecycle status values.

## 10. Lint Design

Lint rules are advisory unless configured as errors.

Initial lint rules:

| Rule ID | Description | Default Severity |
| --- | --- | --- |
| `SAC-LINT-001` | Description must be meaningful and not empty. | error |
| `SAC-LINT-002` | Owner must be present. | error |
| `SAC-LINT-003` | Steward should be present for governed objects. | warning |
| `SAC-LINT-004` | Critical objects should define quality expectations. | warning |
| `SAC-LINT-005` | AI context should be present for entities and metrics. | warning |
| `SAC-LINT-006` | Names should use consistent casing. | warning |

## 11. Generator Design

Generators consume the registry and produce output artifacts. Generators must not parse files independently.

Generator interface:

```text
name
description
supported_object_kinds
validate_compatibility(registry)
generate(registry, output_path, options)
```

Version 0.1 generator:

- Markdown documentation.

Planned generators:

- Mermaid diagrams.
- HTML documentation.
- AI context files.
- dbt Semantic Layer.
- OpenMetadata import files.
- Power BI semantic model scaffolding.
- Knowledge graph triples.
- OpenAPI extensions.

## 12. Markdown Documentation Generator

The MVP documentation generator should create:

- `index.md`
- `domains.md`
- `entities.md`
- `metrics.md`
- `glossary.md`
- `relationships.md`

Each generated page should include:

- Object name.
- Description.
- Owner and steward.
- Domain.
- Governance classification.
- Relationships.
- Quality expectations.
- AI context where available.
- Source file path.

## 13. Testing Strategy

### 13.1 Unit Tests

Cover:

- YAML loading.
- Schema selection.
- Registry construction.
- Reference resolution.
- Lint rules.
- Generator output formatting.

### 13.2 Integration Tests

Cover:

- Valid supply chain example passes validation.
- Invalid fixtures fail with expected rule ids.
- Markdown generator creates expected files.
- GitHub Actions command matches local validation command.

### 13.3 Compatibility Tests

Future vendor adapters should include fixtures proving that generated outputs remain stable for known input definitions.

## 14. CI/CD Design

GitHub Actions should run on pull requests and pushes to `main`.

Initial workflow:

```text
checkout
set up runtime
install dependencies
run unit tests
run semantics validate examples/
run semantics lint examples/
generate markdown docs
```

## 15. Implementation Language Recommendation

Python is recommended for Version 0.1 because:

- YAML, JSON Schema, and CLI tooling are mature.
- Data and governance teams are likely to understand it.
- Packaging a CLI is straightforward.
- It integrates well with documentation and validation workflows.

Suggested libraries:

- `typer` for CLI.
- `pydantic` or `dataclasses` for internal models.
- `pyyaml` or `ruamel.yaml` for YAML parsing.
- `jsonschema` for schema validation.
- `pytest` for tests.

This is a recommendation, not a permanent architectural constraint.

## 16. Extension Model

The core schema should reserve an `extensions` object on each semantic object.

Example:

```yaml
extensions:
  databricks:
    catalog: main
    schema: gold
  openmetadata:
    glossary: Enterprise Glossary
```

Extension rules:

- Extensions must be namespaced.
- Extensions must not override required core fields.
- Generators may ignore unknown extensions.
- Vendor adapters may validate their own extension namespace.

## 17. Versioning Strategy

Version 0.1 should introduce:

- Project version in package metadata.
- Specification version in schemas.
- Optional `spec_version` field in semantic package metadata.

Breaking schema changes should require a new minor or major specification version once the project reaches 1.0.

## 18. Design Decisions

| Decision | Choice | Reason |
| --- | --- | --- |
| Primary source format | YAML | Human-readable and Git-friendly. |
| Schema format | JSON Schema | Broad tooling and editor support. |
| Runtime posture | No semantic runtime | Keeps project complementary to existing platforms. |
| MVP generator | Markdown | Useful immediately and easy to verify. |
| Extension mechanism | Namespaced `extensions` object | Supports vendors without polluting the core spec. |
| MVP industry example | Supply Chain | Demonstrates entities, metrics, relationships, quality, and governance clearly. |

## 19. Open Design Questions

- Should semantic packages have a required `semantics.yaml` manifest?
- Should relationship definitions be separate files, embedded fields, or both?
- Should metric formulas use target platform SQL, a neutral expression language, or both?
- Should the CLI support remote package dependencies in Version 0.2?
- Should generated docs be committed or treated as build artifacts?

