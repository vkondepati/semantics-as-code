from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

import typer


@dataclass
class Diagnostic:
    severity: str
    rule_id: str
    message: str
    path: Optional[Path] = None
    object_id: Optional[str] = None
    suggestion: Optional[str] = None

    def format(self) -> str:
        location = str(self.path) if self.path else "<project>"
        subject = f" ({self.object_id})" if self.object_id else ""
        text = f"{location}{subject} [{self.rule_id}] {self.severity.upper()}: {self.message}"
        if self.suggestion:
            text += f"\nSuggestion: {self.suggestion}"
        return text


def print_diagnostics(diagnostics: Iterable[Diagnostic]) -> None:
    count = 0
    for diagnostic in diagnostics:
        count += 1
        typer.echo(diagnostic.format())
    if count == 0:
        typer.echo("No issues found.")
