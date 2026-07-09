from pathlib import Path
from typing import Optional

import typer

from semantics.core.errors import Diagnostic, print_diagnostics
from semantics.generators.markdown import generate_markdown
from semantics.linters.rules import lint_registry
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
def lint(path: Path = typer.Argument(Path("."), help="Semantic package path.")) -> None:
    """Run advisory and required semantic lint rules."""
    diagnostics, registry = validate_path(path)
    if not any(d.severity == "error" for d in diagnostics):
        diagnostics.extend(lint_registry(registry))
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

    if target != "markdown":
        print_diagnostics(
            [
                Diagnostic(
                    severity="error",
                    rule_id="SAC-GEN-001",
                    message=f'Unsupported generator target "{target}". Supported targets: markdown.',
                )
            ]
        )
        raise typer.Exit(code=2)

    generated = generate_markdown(registry, output)
    typer.echo(f"Generated {len(generated)} Markdown files in {output}")


@app.command()
def test(path: Path = typer.Argument(Path("."), help="Semantic package path.")) -> None:
    """Planned command for executable semantic tests."""
    typer.echo("semantics test is planned for a future release. Use validate and lint in Version 0.1.")


@app.command()
def diff(
    base: Optional[str] = typer.Option(None, "--base", help="Base ref."),
    head: Optional[str] = typer.Option(None, "--head", help="Head ref."),
) -> None:
    """Planned command for comparing semantic package changes."""
    _ = (base, head)
    typer.echo("semantics diff is planned for a future release.")
