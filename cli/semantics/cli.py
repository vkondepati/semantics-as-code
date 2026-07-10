from pathlib import Path
from typing import Optional

import typer

from semantics.core.errors import Diagnostic, print_diagnostics
from semantics.core.diff import diff_paths
from semantics.generators.registry import GENERATORS, supported_targets
from semantics.linters.rules import lint_registry, load_lint_config
from semantics.validators.validate import validate_path

app = typer.Typer(help="Validate, lint, and generate enterprise semantics as code.")


@app.command()
def validate(path: Path = typer.Argument(Path("."), help="Semantic package path.")) -> None:
    """Validate YAML syntax, schemas, and cross-references."""
    diagnostics, _registry = validate_path(path)
    print_diagnostics(diagnostics)
    if any(d.severity == "error" for d in diagnostics):
        raise typer.Exit(code=1)


@app.command()
def lint(
    path: Path = typer.Argument(Path("."), help="Semantic package path."),
    config: Optional[Path] = typer.Option(None, "--config", "-c", help="Optional lint config or package manifest path."),
) -> None:
    """Run advisory and required semantic lint rules."""
    diagnostics, registry = validate_path(path)
    if not any(d.severity == "error" for d in diagnostics):
        diagnostics.extend(lint_registry(registry, load_lint_config(path, config)))
    print_diagnostics(diagnostics)
    if any(d.severity == "error" for d in diagnostics):
        raise typer.Exit(code=1)


@app.command()
def generate(
    path: Path = typer.Argument(Path("."), help="Semantic package path."),
    target: str = typer.Option("markdown", "--target", "-t", help="Generator target."),
    output: Path = typer.Option(Path("dist/docs"), "--output", "-o", help="Output directory."),
) -> None:
    """Generate artifacts from semantic definitions."""
    diagnostics, registry = validate_path(path)
    if any(d.severity == "error" for d in diagnostics):
        print_diagnostics(diagnostics)
        raise typer.Exit(code=1)

    generator = GENERATORS.get(target)
    if generator is None:
        print_diagnostics(
            [
                Diagnostic(
                    severity="error",
                    rule_id="SAC-GEN-001",
                    message=f'Unsupported generator target "{target}". Supported targets: {supported_targets()}.',
                )
            ]
        )
        raise typer.Exit(code=2)

    generated = generator(registry, output)
    typer.echo(f"Generated {len(generated)} {target} files in {output}")


@app.command()
def test(path: Path = typer.Argument(Path("."), help="Semantic package path.")) -> None:
    """Planned command for executable semantic tests."""
    typer.echo("semantics test is planned for a future release. Use validate and lint in Version 0.1.")


@app.command()
def diff(
    base: Path = typer.Option(..., "--base", help="Base semantic package path."),
    head: Path = typer.Option(..., "--head", help="Head semantic package path."),
) -> None:
    """Compare two semantic package paths."""
    result = diff_paths(base, head)
    if result.diagnostics:
        print_diagnostics(result.diagnostics)
    if any(d.severity == "error" for d in result.diagnostics):
        raise typer.Exit(code=1)

    if not result.has_changes:
        typer.echo("No semantic changes found.")
        return

    for label, values in (("Added", result.added), ("Removed", result.removed), ("Changed", result.changed)):
        if values:
            typer.echo(f"{label}:")
            for value in values:
                typer.echo(f"  - {value}")
