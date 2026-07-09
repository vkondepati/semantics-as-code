# Contributing

Thanks for helping build Semantics as Code.

## Development Setup

```bash
pip install -e ".[dev]"
pytest
```

## Local Checks

```bash
semantics validate examples/supply-chain
semantics lint examples/supply-chain
semantics generate examples/supply-chain --target markdown --output dist/docs
```

## Contribution Guidelines

- Keep the core specification vendor neutral.
- Put vendor-specific metadata under namespaced `extensions`.
- Add tests for schema, validation, linting, and generator changes.
- Keep examples readable to business and technical users.
- Update docs when changing fields, commands, or generated output.

## Pull Request Checklist

- Tests pass.
- Supply chain example validates.
- README or docs are updated when behavior changes.
- New schema fields include examples or templates.
