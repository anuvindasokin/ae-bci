# AE-BCI: Acoustoelectric Heterodyne Neural Recording

[![Python tests](https://github.com/anuvindasokin/ae-bci/actions/workflows/python-tests.yml/badge.svg)](https://github.com/anuvindasokin/ae-bci/actions/workflows/python-tests.yml)

AE-BCI is an early-stage experimental platform investigating whether focused
ultrasound can spatially localise controlled electrical activity through the
acoustoelectric effect. It combines a calibrated acoustic carrier, a passive
neural-equivalent electrical dipole, differential carrier-band sensing,
coherent lock-in demodulation, spatial scanning, and reproducible analysis.

> [!WARNING]
> **Phantom-only restriction:** all current designs, procedures, and settings are
> exclusively for conductive saline tanks, synthetic tissue-equivalent phantoms,
> synthetic skulls, and appropriately controlled ex-vivo materials. The system
> must not be connected to, implanted in, positioned on, or tested with a person
> or animal. This repository does not describe a medical device or a proven BCI.

## Research concept

Acoustic pressure may produce a small local conductivity change,
`Δσ / σ = K × P`. An electrical source at `fE` interacting with an acoustic
carrier at `fA` can produce sidebands at `fA − fE` and `fA + fE`. A lock-in
referenced coherently to `fA` recovers signed baseband information from X and Y.
A carrier-band response alone is not evidence of acoustoelectric localisation.

The source bandwidth is **10 Hz to 8 kHz** (preferred driver design margin:
approximately 5 Hz to at least 10 kHz). Carrier configurations are frequency
flexible: 500 kHz is an initial baseline, while 650 kHz, 750 kHz, 1 MHz, and
other selected frequencies each require independent hardware validation and
calibration. A transducer is never assumed to work outside its validated range.

## Architecture

```text
coherent carrier source → linear RF amplifier → power monitoring
→ frequency-specific matching → calibrated focused transducer
→ conductive phantom + externally driven passive PtIr dipole
→ differential PtIr receiver → carrier-band front end
→ X/Y lock-in demodulation → analysis and spatial reconstruction
```

The minimum control set includes baseline, source-only, ultrasound-only,
combined, acoustic-blocked, dummy-load, polarity-reversed, displaced-source,
displaced-receiver, and frequency-shifted conditions. See the
[control matrix](docs/experiments/control-experiments.md).

## Repository map

- `docs/`: theory, architecture, subsystem requirements, calibration, safety,
  experimental plans, and development status.
- `hardware/`: requirements and unpopulated design/calibration release areas.
- `software/ae_bci/`: reusable analysis and validation package.
- `software/tests/`: unit tests for frequency-flexible computations and schemas.
- `protocols/`, `logs/`, and `data/`: reproducibility templates and rules.

## Quick start

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
pytest
ruff check .
mkdocs serve
```

Examples:

```bash
ae-bci-sidebands 650000 8000
ae-bci-validate data/metadata/experiment-metadata-template.yaml
python software/scripts/calculate_sidebands.py 750000 1000
```

Specifications without evidence are marked `TBD`. No measurements, simulations,
citations, manufacturer part numbers, or component selections are fabricated.

**License status: TBD.** Separate terms may be required for software, hardware,
documentation, mechanical designs, and data. See [LICENSES/README.md](LICENSES/README.md).

## Current validation status

- Documentation and software scaffold: implemented.
- Software unit tests: automated in CI; run locally before relying on results.
- Hardware fabrication and calibration: not completed.
- Acoustoelectric experiments: not completed.
- Biological performance and medical safety: not evaluated.

