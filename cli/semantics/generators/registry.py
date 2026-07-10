from pathlib import Path
from typing import Callable, Dict, List

from semantics.core.registry import Registry
from semantics.generators.ai_context import generate_ai_context
from semantics.generators.dbt import generate_dbt
from semantics.generators.html import generate_html
from semantics.generators.markdown import generate_markdown
from semantics.generators.mermaid import generate_mermaid
from semantics.generators.openmetadata import generate_openmetadata

Generator = Callable[[Registry, Path], List[Path]]

GENERATORS: Dict[str, Generator] = {
    "markdown": generate_markdown,
    "mermaid": generate_mermaid,
    "html": generate_html,
    "dbt": generate_dbt,
    "openmetadata": generate_openmetadata,
    "ai-context": generate_ai_context,
    "ai_context": generate_ai_context,
}


def supported_targets() -> str:
    return ", ".join(sorted(GENERATORS))
