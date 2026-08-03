"""Project logging setup."""

import logging


def configure_logging(level: int = logging.INFO) -> None:
    """Configure concise deterministic console logging."""
    logging.basicConfig(level=level, format="%(levelname)s %(name)s: %(message)s")

