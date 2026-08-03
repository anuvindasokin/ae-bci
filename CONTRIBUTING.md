# Contributing

Use Python 3.11 or newer, SI units, type hints, docstrings, and tests. Branch names
should use `feature/`, `hardware/`, `docs/`, `experiment/`, `analysis/`, or `fix/`.
Use conventional commits such as `docs(neural-source): document dipole geometry`.

Never alter raw data, fabricate measurements, present proposals as validated
hardware, or weaken the phantom-only restriction. Link claims to permitted source
material or project data. Mark unknown specifications `TBD`.

Before opening a pull request, run `pytest`, `ruff check .`, and `mkdocs build
--strict`. Describe evidence, assumptions, controls, data provenance, safety
impact, and validation status in the pull request.

