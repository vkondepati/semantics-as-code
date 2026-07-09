# Product Requirements Document: Semantics as Code

## 1. Product Summary

Semantics as Code is an open-source, vendor-neutral specification and starter kit for defining enterprise business semantics as version-controlled, testable, deployable code.

The project enables organizations to define business entities, metrics, dimensions, relationships, rules, governance metadata, quality expectations, glossary terms, synonyms, AI context, and knowledge graph mappings in human-readable YAML. Those definitions can then be validated, documented, tested, and transformed into platform-specific artifacts for tools such as dbt, Databricks, Snowflake, Microsoft Fabric, OpenMetadata, Power BI, and other semantic or metadata systems.

Semantics as Code is not a semantic runtime, metadata catalog, BI tool, governance platform, or metric engine. It is the common open specification that existing platforms can consume, generate, or interoperate with.

## 2. Problem Statement

Enterprise business semantics are rarely managed as software artifacts. While infrastructure, pipelines, APIs, policies, and observability can be standardized through code-first approaches such as Terraform, dbt, OpenAPI, Policy as Code, and OpenTelemetry, business meaning often remains scattered across PowerPoint, Excel, Confluence, wikis, PDFs, and tribal knowledge.

This creates inconsistent definitions of core concepts such as Customer, Revenue, Product, Inventory, Order, Supplier, Region, and KPIs. The result is duplicated metrics, contradictory dashboards, low trust in analytics, weak governance, and unreliable AI-generated answers.

Organizations need a way to define enterprise semantics once, version them in Git, validate them in CI/CD, and generate artifacts for multiple downstream platforms without rewriting definitions for each vendor.

## 3. Vision

Make business semantics a first-class software artifact.

Semantics as Code should become the de facto open specification, blueprint, template library, and reference implementation for enterprise semantic modeling. It should allow organizations to author business meaning once and generate vendor-specific outputs across analytics, governance, metadata, documentation, knowledge graph, and AI contexts.

## 4. Goals

- Provide a vendor-neutral YAML specification for enterprise business semantics.
- Enable Git-first semantic modeling with validation, linting, testing, and generation workflows.
- Supply starter templates and examples for common enterprise domains and industries.
- Generate documentation, diagrams, glossary assets, metric definitions, semantic model artifacts, knowledge graph mappings, and AI context files.
- Complement existing tools rather than competing with semantic layers, catalogs, BI platforms, or metric engines.
- Establish a clear comparison matrix that explains what the project is and is not.

## 5. Non-Goals

- Do not build a BI visualization tool.
- Do not build a query engine or metric runtime.
- Do not replace dbt Semantic Layer, Cube, AtScale, LookML, Power BI, Databricks, Snowflake, Microsoft Fabric, OpenMetadata, or similar platforms.
- Do not require a specific warehouse, lakehouse, catalog, graph database, or orchestration framework.
- Do not create a proprietary hosted SaaS as the primary product experience.
- Do not force a single enterprise domain model across all organizations.

## 6. Target Users

### Primary Users

- Data architects defining enterprise semantic standards.
- Analytics engineers maintaining metrics, dimensions, and semantic models.
- Data governance teams managing glossary terms, ownership, stewardship, classification, and policy metadata.
- Data product teams publishing reusable business definitions.
- Platform teams building semantic model generation and validation pipelines.

### Secondary Users

- BI developers consuming generated semantic artifacts.
- Data scientists and AI engineers using semantic context for retrieval and AI applications.
- Enterprise architects aligning business capabilities, entities, and data products.
- Open-source contributors extending schemas, templates, validators, and generators.

## 7. Core Use Cases

1. Define enterprise entities such as Customer, Product, Order, Supplier, Region, and Inventory in YAML.
2. Define governed metrics such as Revenue, Gross Margin, Churn Rate, Fill Rate, and On-Time Delivery.
3. Define relationships across entities and domains.
4. Attach ownership, stewardship, classification, PII, quality expectations, and business rules to semantic definitions.
5. Validate semantic YAML in local development and CI/CD.
6. Generate documentation, business glossaries, diagrams, and AI context files.
7. Generate downstream artifacts for semantic, metadata, BI, and governance platforms.
8. Compare semantic definition changes across branches or releases.
9. Bootstrap semantic modeling using industry-specific starter kits.

## 8. Product Principles

- Vendor neutral.
- Git first.
- YAML based.
- Human readable.
- Machine consumable.
- Composable.
- Extensible.
- AI friendly.
- CI/CD ready.
- Open standard.

## 9. Functional Requirements

### 9.1 Semantic Specification

The product must define YAML schemas for:

- Business entities.
- Metrics.
- Dimensions.
- Relationships.
- Domains.
- Business rules.
- Glossary terms.
- Synonyms.
- Governance metadata.
- Security classifications.
- Data quality expectations.
- AI context.
- Knowledge graph mappings.

Each specification object must support common metadata, including:

- Stable identifier.
- Display name.
- Description.
- Owner.
- Steward.
- Domain.
- Tags.
- Version.
- Lifecycle status.
- Source file path.

### 9.2 Entity Definitions

The product must support entity definitions that include:

- Entity name and display name.
- Business description.
- Business key.
- Canonical table or source reference.
- Owner and steward.
- Classification and PII flags.
- Relationships to other entities.
- Synonyms.
- Business rules.
- Quality expectations.
- Knowledge graph mapping.
- AI context.

### 9.3 Metric Definitions

The product must support metric definitions that include:

- Metric name.
- Description.
- Owner.
- Formula.
- Grain.
- Dimensions.
- Filters.
- Source references.
- Quality expectations.
- Governance metadata.
- Synonyms and glossary mappings.

### 9.4 Validation and Linting

The CLI must support:

- `semantics validate`
- `semantics lint`
- `semantics test`
- `semantics generate`
- `semantics diff`

Validation must check:

- YAML syntax.
- Schema compliance.
- Required fields.
- Identifier uniqueness.
- Broken references.
- Invalid relationship targets.
- Unsupported classification values.
- Metric formula structure where possible.
- Generator compatibility warnings.

Linting should check:

- Naming conventions.
- Description completeness.
- Ownership completeness.
- Missing governance metadata.
- Missing AI context.
- Missing quality expectations for critical entities or metrics.

### 9.5 Generators

The product should generate:

- Business glossary documentation.
- Metric views.
- dbt Semantic Layer artifacts.
- Power BI semantic model scaffolding.
- Mermaid diagrams.
- Knowledge graph outputs.
- OpenMetadata-compatible imports.
- Markdown documentation.
- HTML documentation.
- AI context files.
- JSON Schema.
- OpenAPI extensions.

Generators must be modular so vendor-specific adapters can be added without changing the core specification.

### 9.6 Starter Kits and Templates

The repository must include starter examples for:

- Supply Chain.
- Retail.
- Banking.
- Healthcare.
- Manufacturing.
- Energy.
- Insurance.
- Telecommunications.
- Public Sector.

Templates must include examples for:

- Entity.
- Metric.
- Domain.
- Glossary term.
- Relationship.
- Governance classification.
- Quality expectation.
- Knowledge graph mapping.

### 9.7 Documentation

The project must include documentation for:

- Project purpose.
- Installation.
- Repository structure.
- Specification overview.
- YAML object reference.
- CLI usage.
- Generator usage.
- Contributor guide.
- Comparison matrix.
- Roadmap.

The README must clearly communicate that Semantics as Code complements existing platforms and is not another semantic layer, metadata catalog, BI tool, or governance runtime.

### 9.8 CI/CD

The project must provide GitHub Actions workflows for:

- Validating YAML.
- Running lint checks.
- Running semantic tests.
- Generating documentation.
- Generating diagrams.
- Publishing documentation artifacts.

### 9.9 VS Code Extension

The product should provide or plan a VS Code extension supporting:

- Syntax highlighting.
- Schema validation.
- Autocomplete.
- Relationship navigation.
- Diagram preview.

## 10. Repository Structure

The target repository structure should be:

```text
semantics-as-code/
  docs/
  schemas/
  entities/
  metrics/
  domains/
  governance/
  quality/
  knowledge_graph/
  templates/
  examples/
  generators/
  validation/
  cli/
  sdk/
  vscode-extension/
  .github/
  README.md
```

## 11. Example Definitions

### Entity Example

```yaml
entity: Customer
display_name: Customer
description: Master customer entity.
business_key: customer_id
owner: Sales
steward: Data Governance
classification: Confidential
pii: true
canonical_table: gold.customer
relationships:
  - Orders
  - Addresses
  - Contracts
synonyms:
  - Client
  - Buyer
business_rules:
  - customer_id cannot change
  - inactive customers retained for 7 years
quality:
  - completeness > 99%
knowledge_graph: Customer
ai_context: Represents the purchasing organization.
```

### Metric Example

```yaml
metric: Revenue
owner: Finance
description: Recognized revenue.
formula: SUM(net_sales)
grain: Order
dimensions:
  - Customer
  - Product
  - Date
filters:
  - status = Completed
quality:
  - reconciles with ERP
```

## 12. Comparison Matrix Requirement

The README must include a comparison matrix from the first public release.

| Capability | OpenMetadata | dbt Semantic Layer | Databricks Metric Views | Snowflake OSI | Semantics as Code |
| --- | --- | --- | --- | --- | --- |
| Business glossary | Yes | Partial | No | Partial | Yes |
| Vendor neutral | Yes | Partial | No | Yes | Yes |
| Version-controlled in Git | Partial | Yes | Partial | Partial | Yes |
| Deployable as code | Partial | Yes | Yes | Partial | Yes |
| Enterprise semantic blueprint | No | No | No | No | Yes |
| Starter templates | Limited | Limited | No | No | Yes |
| Multi-platform artifact generation | No | No | No | No | Yes |

## 13. MVP Scope

Version 0.1 must deliver:

- Core specification for entities, metrics, domains, glossary terms, relationships, governance metadata, quality expectations, and AI context.
- JSON Schemas for core YAML files.
- Starter repository structure.
- Starter templates.
- At least one complete industry example.
- CLI validation command.
- Basic lint rules.
- Markdown documentation generation.
- README with comparison matrix.
- GitHub Actions workflow for validation.

Version 0.1 should not attempt to deliver full vendor adapters, a complete VS Code extension, or a production-grade knowledge graph generator.

## 14. Roadmap

### Version 0.1

- Specification.
- Starter kit.
- Templates.
- Validation.
- Basic documentation.
- Comparison matrix.

### Version 0.2

- Generators.
- Documentation site.
- Metric view generation.
- Expanded examples.

### Version 0.5

- Knowledge graph generation.
- AI context generation.
- OpenMetadata integration.
- dbt integration.

### Version 1.0

- Vendor adapters for Databricks, Snowflake, Fabric, BigQuery, OpenMetadata, Apache Polaris, Apache Iceberg, and Apache Gravitino.
- Stable specification versioning.
- Compatibility test suite.
- Extension points for third-party generators.

## 15. Success Metrics

- Organizations can define core enterprise semantics once and generate artifacts for at least three downstream platforms.
- The specification supports representative enterprise examples across at least five industries.
- CLI validation can run locally and in GitHub Actions.
- Contributors can add new templates, examples, schemas, and generators without changing the core architecture.
- README and documentation clearly differentiate the project from semantic layers, metadata catalogs, BI tools, and metric engines.
- The project gains adoption as an open specification for enterprise semantic modeling.

## 16. Acceptance Criteria

- A new user can clone the repository, inspect examples, and understand the project purpose within five minutes.
- A user can author an entity and metric definition in YAML and validate both from the CLI.
- Invalid YAML or broken semantic references fail validation with actionable error messages.
- Generated documentation includes entities, metrics, relationships, owners, governance metadata, and AI context.
- The README includes a comparison matrix and clear positioning against adjacent tools.
- CI/CD validates semantic definitions on pull requests.
- The specification is documented well enough for a third-party tool to consume or generate Semantics as Code YAML.

## 17. Risks and Mitigations

| Risk | Mitigation |
| --- | --- |
| Scope expands into building a full semantic platform | Keep specification and generators separate from runtime execution. |
| Vendor adapters become tightly coupled to core schemas | Use adapter interfaces and compatibility tests. |
| YAML becomes too verbose for real users | Provide templates, examples, defaults, and schema-driven autocomplete. |
| Project overlaps confusingly with existing tools | Maintain comparison matrix and explicit non-goals. |
| Enterprise semantics vary too widely across industries | Use composable schemas and optional extension fields. |
| AI context becomes ungoverned free text | Attach AI context to governed semantic objects with ownership and review workflows. |

## 18. Open Questions

- What schema versioning strategy should be used for breaking changes?
- Should the primary CLI be implemented in Python, TypeScript, Go, or another language?
- Should formulas use a custom expression grammar or defer to target platform syntax?
- What is the minimum viable adapter interface for generators?
- How should semantic packages be shared across repositories?
- Should the project define a formal extension registry for vendor and industry-specific fields?

