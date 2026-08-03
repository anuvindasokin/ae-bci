"""Analysis provenance helpers."""

import subprocess
from pathlib import Path


def git_commit(repository: str | Path = ".") -> str:
    """Return the current Git commit without changing repository state."""
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repository,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()

