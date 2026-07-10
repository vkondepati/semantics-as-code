# Specification Versioning

Semantics as Code uses semantic versioning for the specification and the reference implementation.

## Version Fields

- `spec_version` appears in `semantic_package` manifests and identifies the schema contract used by a package.
- `version` appears on each semantic object and identifies the object definition version.
- The Python package version identifies the reference CLI implementation version.

## Compatibility Policy

- Patch releases may clarify documentation, add tests, and fix generator defects without changing valid YAML.
- Minor releases may add optional fields, new generators, new lint rules, and new adapters.
- Major releases may remove fields, rename fields, or change validation behavior in a way that can reject previously valid packages.

## Stability Rules

- Core fields remain portable across vendors.
- Vendor-specific fields belong under namespaced `extensions`.
- Generators may ignore unknown extensions.
- Adapters must not require changes to the core object model.
- New object kinds require a schema and compatibility test fixture.

## Current Stable Contract

The current stable contract supports:

- `semantic_package`
- `domain`
- `entity`
- `metric`
- `glossary_term`
- `relationship`
- `quality_expectation`
