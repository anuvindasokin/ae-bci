"""Dataset integrity checks."""

from hashlib import sha256
from pathlib import Path


def file_sha256(path: str | Path) -> str:
    """Return a file's SHA-256 digest without modifying it."""
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(file_path)
    digest = sha256()
    with file_path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_dataset_files(paths: list[str | Path]) -> dict[str, str]:
    """Require unique files and return stable integrity hashes."""
    resolved = [Path(path).resolve() for path in paths]
    if not resolved:
        raise ValueError("At least one dataset file is required.")
    if len(set(resolved)) != len(resolved):
        raise ValueError("Dataset file list contains duplicates.")
    return {str(path): file_sha256(path) for path in resolved}

