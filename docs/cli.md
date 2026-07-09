# CLI

The `semantics` CLI validates, lints, and generates artifacts from semantic packages.

## Install for Development

```bash
pip install -e ".[dev]"
```

## Validate

```bash
semantics validate examples/supply-chain
```

Validation checks YAML syntax, JSON Schema compliance, duplicate ids, missing references, classifications, and statuses.

## Lint

```bash
semantics lint examples/supply-chain
```

Linting checks description quality, ownership, stewardship, quality expectations, AI context, and naming consistency.

## Generate

```bash
semantics generate examples/supply-chain --target markdown --output dist/docs
```

Version 0.1 supports the `markdown` target.

## Exit Codes

| Code | Meaning |
| --- | --- |
| `0` | Success. |
| `1` | Validation, lint, or generation failure. |
| `2` | Invalid CLI arguments or unsupported target. |
