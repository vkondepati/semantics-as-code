# Specification

Semantics as Code definitions are YAML files with a required `kind` field. The current reference implementation supports semantic packages, domains, entities, metrics, glossary terms, relationships, and quality expectations.

## Common Fields

| Field | Required | Description |
| --- | --- | --- |
| `id` | Yes | Stable identifier for references and generated artifacts. |
| `kind` | Yes | Object type such as `entity` or `metric`. |
| `name` | Yes | Human-readable semantic name. |
| `display_name` | Yes | Label for documentation and generated outputs. |
| `description` | Most objects | Business description. |
| `owner` | Yes | Accountable business or data owner. |
| `steward` | Recommended | Day-to-day steward or governance owner. |
| `domain` | Recommended | Business domain reference. |
| `version` | Yes | Definition version. |
| `status` | Recommended | `draft`, `active`, `deprecated`, or `retired`. |
| `classification` | Optional | `Public`, `Internal`, `Confidential`, or `Restricted`. |
| `extensions` | Optional | Namespaced vendor or organization metadata. |

## Semantic Package Manifest

A package can include `semantics.yaml` at its root.

```yaml
id: supply-chain
kind: semantic_package
name: Supply Chain
display_name: Supply Chain
description: Supply chain starter semantic package.
owner: Data Governance
version: 0.2.0
spec_version: 0.2.0
lint:
  rules:
    SAC-LINT-005: warning
extensions: {}
```

The manifest can configure lint severities with `off`, `warning`, or `error`.

## Extension Model

Use `extensions` for fields that are not part of the portable core.

```yaml
extensions:
  databricks:
    catalog: main
  openmetadata:
    glossary: Enterprise Glossary
```

Generators may ignore unknown extension namespaces.
