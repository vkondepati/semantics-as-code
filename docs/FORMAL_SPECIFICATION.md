# Semantics as Code Formal Specification

## Status

Version: 1.0.0 reference specification.

This document defines the portable semantic contract implemented by the reference CLI.

## Package

A Semantics as Code package is a directory containing YAML semantic object definitions. A package should include a root `semantics.yaml` manifest with `kind: semantic_package`.

Packages may declare local dependencies:

```yaml
dependencies:
  - name: shared-domain
    path: ../shared-domain
    version: 1.0.0
```

Dependency paths are resolved relative to the package manifest.

## Object Identity

Every semantic object must define:

- `id`
- `kind`
- `name`
- `display_name`
- `version`

Object ids are unique within the loaded package graph.

## Supported Object Kinds

- `semantic_package`
- `domain`
- `entity`
- `metric`
- `glossary_term`
- `relationship`
- `quality_expectation`

## Reference Rules

- Object references may use `id`, `name`, or `display_name`.
- Domain references must resolve to `domain`.
- Metric grains and dimensions must resolve to semantic objects.
- Metric glossary terms must resolve to `glossary_term`.
- Relationship endpoints must resolve to semantic objects.
- Quality expectation targets must resolve to semantic objects.

## Metric Formula Rules

Metric formulas are portable expressions, not executable SQL statements.

Allowed:

- Arithmetic operators: `+`, `-`, `*`, `/`
- Parentheses
- Function-like calls such as `SUM(amount)` and `COUNT(order_id)`
- Comparison operators in simple expressions

Disallowed:

- Statement separators such as `;`
- SQL comments such as `--`, `/*`, or `*/`
- Unbalanced parentheses
- Unsupported control characters

## Extension Rules

Vendor and organization-specific fields must be placed under `extensions`.

```yaml
extensions:
  databricks:
    catalog: main
  openmetadata:
    glossary: Enterprise Glossary
```

Unknown extension namespaces must not invalidate a portable semantic object.
