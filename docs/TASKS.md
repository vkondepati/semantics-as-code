# Implementation Tasks: Semantics as Code

## 1. Version 0.1 Objective

Deliver a usable open-source starter kit for defining, validating, linting, and documenting enterprise semantics as YAML.

Version 0.1 is complete when a user can:

- Clone the repository.
- Read the README and understand the project.
- Inspect templates and a complete supply chain example.
- Author an entity and metric in YAML.
- Run CLI validation and linting.
- Generate Markdown documentation.
- Run the same checks in GitHub Actions.

## 2. Milestone Plan

| Milestone | Outcome |
| --- | --- |
| M1: Repository foundation | Project structure, README, docs, and contribution basics exist. |
| M2: Core specification | JSON Schemas and YAML templates define the MVP semantic objects. |
| M3: Example package | Supply chain starter kit validates successfully. |
| M4: CLI validation | `semantics validate` and `semantics lint` work locally. |
| M5: Documentation generation | `semantics generate --target markdown` creates readable docs. |
| M6: CI/CD | Pull requests run validation, linting, tests, and generation checks. |

## 3. Task Backlog

### M1: Repository Foundation

- [x] Create target repository folders:
  - `schemas/`
  - `templates/`
  - `examples/`
  - `cli/`
  - `tests/`
  - `.github/workflows/`
- [x] Expand `README.md` with:
  - Project summary.
  - Problem statement.
  - What this project is.
  - What this project is not.
  - Quick start.
  - Repository structure.
  - Comparison matrix.
  - Roadmap summary.
- [x] Add `CONTRIBUTING.md`.
- [x] Add `CODE_OF_CONDUCT.md`.
- [x] Add `docs/specification.md`.
- [x] Add `docs/cli.md`.
- [x] Add `docs/generators.md`.
- [x] Add `docs/examples.md`.

Acceptance checks:

- [x] A new reader can understand the project from the README without opening the PRD.
- [x] The comparison matrix is present in the README.
- [x] Empty placeholder directories are avoided unless they contain useful starter files.

### M2: Core Specification

- [x] Define common semantic object fields:
  - `id`
  - `kind`
  - `name`
  - `display_name`
  - `description`
  - `owner`
  - `version`
  - `domain`
  - `steward`
  - `tags`
  - `status`
  - `classification`
  - `source`
  - `extensions`
- [x] Create `schemas/semantic-object.schema.json`.
- [x] Create `schemas/entity.schema.json`.
- [x] Create `schemas/metric.schema.json`.
- [x] Create `schemas/domain.schema.json`.
- [x] Create `schemas/glossary-term.schema.json`.
- [x] Create `schemas/relationship.schema.json`.
- [x] Create `schemas/quality-expectation.schema.json`.
- [x] Define allowed lifecycle statuses.
- [x] Define allowed classification values.
- [x] Add schema examples for each object kind.
- [x] Add template YAML files for each object kind.

Acceptance checks:

- [x] Every schema validates at least one positive fixture.
- [x] Every schema rejects at least one invalid fixture.
- [x] Every template has comments or obvious placeholder values.
- [x] All core schemas include `extensions`.

### M3: Supply Chain Example Package

- [x] Create `examples/supply-chain/README.md`.
- [x] Add supply chain domains:
  - Sales.
  - Procurement.
  - Inventory.
  - Logistics.
  - Finance.
- [x] Add core entities:
  - Customer.
  - Product.
  - Order.
  - Supplier.
  - Inventory Item.
  - Warehouse.
  - Shipment.
  - Region.
- [x] Add core metrics:
  - Revenue.
  - Gross Margin.
  - On-Time Delivery Rate.
  - Inventory Turnover.
  - Fill Rate.
  - Supplier Defect Rate.
- [x] Add glossary terms for core business concepts.
- [x] Add relationships across entities.
- [x] Add quality expectations for critical entities and metrics.
- [x] Add AI context fields for entities and metrics.

Acceptance checks:

- [x] The supply chain example passes schema validation.
- [x] The supply chain example has no broken references.
- [x] At least three domains, five entities, and three metrics are represented.
- [x] Generated documentation from the example is useful to a business reader.

### M4: CLI Foundation

- [x] Choose CLI implementation language and package structure.
- [x] Create CLI package scaffolding.
- [x] Add local development setup instructions.
- [x] Implement command routing for:
  - `semantics validate`
  - `semantics lint`
  - `semantics generate`
- [x] Implement standard exit codes.
- [x] Implement consistent error formatting.
- [x] Add `--help` output for each command.
- [x] Add package metadata so the CLI can be installed locally.

Acceptance checks:

- [x] Running `semantics --help` shows available commands.
- [x] Running an unknown command returns exit code `2`.
- [x] CLI commands accept a path argument.
- [x] CLI output is readable in local terminals and CI logs.

### M5: YAML Loading and Registry

- [x] Implement recursive YAML file discovery.
- [x] Parse YAML files with source path tracking.
- [x] Select schema based on the `kind` field.
- [x] Build an in-memory semantic registry.
- [x] Normalize object ids.
- [x] Detect duplicate object ids.
- [x] Track object kind, path, and parsed content.
- [x] Add unit tests for registry loading.

Acceptance checks:

- [x] Invalid YAML returns an actionable parse error.
- [x] Duplicate ids fail validation.
- [x] Unknown object kinds fail validation.
- [x] Source file paths appear in error messages.

### M6: Validation

- [x] Implement JSON Schema validation.
- [x] Implement required-field validation through schemas.
- [x] Implement reference validation for:
  - Entity relationships.
  - Metric grain.
  - Metric dimensions.
  - Domain references.
  - Glossary mappings.
  - Quality expectation targets.
- [x] Implement classification validation.
- [x] Implement lifecycle status validation.
- [x] Add invalid fixtures for every validation rule.
- [x] Add tests for every validation rule.

Acceptance checks:

- [x] `semantics validate examples/supply-chain` exits with `0`.
- [x] Invalid fixtures exit with `1`.
- [x] Validation messages include file path, rule id, and message.
- [x] Broken references identify both the source object and missing target.

### M7: Linting

- [x] Implement `SAC-LINT-001`: meaningful description.
- [x] Implement `SAC-LINT-002`: owner required.
- [x] Implement `SAC-LINT-003`: steward recommended for governed objects.
- [x] Implement `SAC-LINT-004`: quality expectations recommended for critical objects.
- [x] Implement `SAC-LINT-005`: AI context recommended for entities and metrics.
- [x] Implement `SAC-LINT-006`: consistent name casing.
- [x] Add severity handling for warnings and errors.
- [x] Add tests for each lint rule.

Acceptance checks:

- [x] `semantics lint examples/supply-chain` exits with `0` or documented warnings only.
- [x] Lint output distinguishes errors from warnings.
- [x] Lint rule ids are stable and documented.

### M8: Markdown Generator

- [x] Implement generator interface.
- [x] Implement Markdown generator target.
- [x] Generate `index.md`.
- [x] Generate `domains.md`.
- [x] Generate `entities.md`.
- [x] Generate `metrics.md`.
- [x] Generate `glossary.md`.
- [x] Generate `relationships.md`.
- [x] Include source file paths in generated docs.
- [x] Include ownership, stewardship, governance, quality, and AI context.
- [x] Add generator tests with snapshot or fixture assertions.

Acceptance checks:

- [x] `semantics generate examples/supply-chain --target markdown --output dist/docs` creates expected files.
- [x] Generated docs include all supply chain entities and metrics.
- [x] Generator fails clearly when the output path is invalid.

### M9: Tests

- [x] Add unit test framework.
- [x] Add positive schema fixtures.
- [x] Add negative schema fixtures.
- [x] Add registry tests.
- [x] Add validation tests.
- [x] Add lint tests.
- [x] Add generator tests.
- [x] Add integration test for the supply chain example.

Acceptance checks:

- [x] Test command passes locally.
- [x] Tests can run without network access.
- [x] Test fixtures are small and easy to understand.

### M10: CI/CD

- [x] Add GitHub Actions workflow at `.github/workflows/validate.yml`.
- [x] Install CLI dependencies.
- [x] Run unit tests.
- [x] Run `semantics validate examples/supply-chain`.
- [x] Run `semantics lint examples/supply-chain`.
- [x] Run Markdown generation as a build check.
- [x] Upload generated docs as an optional artifact.

Acceptance checks:

- [x] Workflow runs on pull requests.
- [x] Workflow runs on pushes to `main`.
- [x] CI fails on invalid YAML.
- [x] CI fails on broken semantic references.

### M11: Documentation

- [x] Document semantic object model.
- [x] Document entity YAML.
- [x] Document metric YAML.
- [x] Document domain YAML.
- [x] Document glossary term YAML.
- [x] Document relationship YAML.
- [x] Document quality expectation YAML.
- [x] Document CLI usage.
- [x] Document generator usage.
- [x] Document extension model.
- [x] Document schema versioning.

Acceptance checks:

- [x] Docs explain all fields used in templates.
- [x] Docs include copy-pasteable examples.
- [x] Docs distinguish Version 0.1 features from roadmap features.

## 4. Version 0.1 Release Checklist

- [x] README is complete.
- [x] PRD is complete.
- [x] Design doc is complete.
- [x] Task backlog is complete.
- [x] Core schemas are present.
- [x] Templates are present.
- [x] Supply chain example is present.
- [x] CLI validates schemas.
- [x] CLI validates cross-references.
- [x] CLI lints semantic definitions.
- [x] CLI generates Markdown docs.
- [x] Tests pass.
- [ ] GitHub Actions workflow passes.
- [x] Release notes are drafted.
- [ ] Version tag is created.

## 5. Version 0.2 Candidate Tasks

- [x] Add Mermaid diagram generator.
- [x] Add HTML documentation generator.
- [x] Add dbt Semantic Layer generator.
- [x] Add OpenMetadata generator.
- [x] Add AI context file generator.
- [x] Add additional industry examples.
- [x] Add semantic package manifest.
- [x] Add configurable lint rules.
- [x] Add `semantics diff`.

## 6. Version 0.5 Candidate Tasks

- [ ] Add knowledge graph generation.
- [ ] Add OpenMetadata integration tests.
- [ ] Add dbt integration tests.
- [ ] Add package dependency support.
- [ ] Add richer metric formula validation.
- [ ] Add VS Code extension prototype.

## 7. Version 1.0 Candidate Tasks

- [ ] Stabilize specification versioning policy.
- [ ] Add compatibility test suite.
- [ ] Add vendor adapter API.
- [ ] Add Databricks adapter.
- [ ] Add Snowflake adapter.
- [ ] Add Fabric adapter.
- [ ] Add BigQuery adapter.
- [ ] Add OpenMetadata adapter.
- [ ] Add Apache Iceberg, Polaris, and Gravitino metadata mappings.
- [ ] Publish formal specification documentation.

## 8. Recommended First Sprint

The first sprint should focus on proving the spine of the project:

- [x] Expand README with positioning and comparison matrix.
- [x] Create core folder structure.
- [x] Create entity, metric, and domain schemas.
- [x] Create entity, metric, and domain templates.
- [x] Create a small supply chain example with three entities and two metrics.
- [x] Implement basic CLI validation.
- [x] Add GitHub Actions validation workflow.

Done means a contributor can make a small YAML change, run validation locally, and see the same validation run in CI.

