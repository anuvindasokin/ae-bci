# Software

Install with `python -m pip install -e ".[dev]"`, test with `pytest`, and lint with
`ruff check .`. Package APIs use SI units and reject invalid inputs rather than
silently changing data. There is intentionally no instrument-control code because
instrument models and interfaces are `TBD`.

