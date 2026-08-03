# Design Decisions

Status for every initial record is **accepted as a project requirement; verification
pending**. Owner, issue, commit, and dates are `TBD`.

## DDR-001: Use 500 kHz as baseline, not exclusive carrier

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

The platform needs an early reference configuration without hard-coding it.

### Options considered

Fixed 500 kHz; frequency-flexible configurations.

### Decision

Use approximately 500 kHz as baseline and support 650 kHz, 750 kHz, 1 MHz, and custom configurations.

### Rationale

This preserves experimental comparison across localisation and transmission trade-offs.

### Consequences

Software is dynamic and hardware records are carrier-specific.

### Verification required

Calibrate every configuration independently.

## DDR-002: Treat carrier configurations independently

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

Transducers and interfaces are frequency dependent.

### Options considered

Assume one broadband chain; validate each chain separately.

### Decision

Each frequency has its own transducer, matching, RF, acoustic, thermal, receiver, lock-in, and artefact records; one transducer is not assumed universal.

### Rationale

Datasheet bandwidth does not establish in-system performance.

### Consequences

Comparisons require complete calibration sets.

### Verification required

Electrical, acoustic, thermal, and system acceptance tests.

## DDR-003: Support 10 Hz–8 kHz electrical sources

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

Arbitrary neural-equivalent test waveforms need defined bandwidth.

### Options considered

Single 8 kHz tone; full 10 Hz–8 kHz usable band.

### Decision

Support 10 Hz–8 kHz, with preferred source-driver margin of approximately 5 Hz to at least 10 kHz.

### Rationale

An upper-band calibration tone is not representative of all supported content.

### Consequences

Source, receiver, lock-in streaming, and software must cover the full band.

### Verification required

Amplitude, phase, delay, current, and waveform-recovery sweeps.

## DDR-004: Use a passive PtIr bipolar source

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

Active electronics inside the phantom add coupling and artefact paths.

### Options considered

Internal active oscillator; external isolated driver with passive dipole.

### Decision

Use a passive PtIr dipole internally, keep active electronics external, use independent bipolar pairs without shared return, and initially activate one orientation.

### Rationale

This makes source current measurable and limits internal complexity.

### Consequences

Feedthrough and cable routes require calibration and controls.

### Verification required

Impedance, bandwidth, offset, leakage, polarity, and orientation tests.

## DDR-005: Use differential intracranial-equivalent sensing

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

Receiver field and common-mode carrier pickup affect spatial response.

### Options considered

Single-ended; differential pair; multi-contact variants.

### Decision

Start with a fixed differential PtIr pair and compare spacing/multi-contact variants later.

### Rationale

Differential sensing provides a controlled initial geometry without claiming optimality.

### Consequences

Geometry, impedance, field sensitivity, cables, CMRR, and transfer function are recorded.

### Verification required

Bench and phantom comparison tests.

## DDR-006: Use coherent dual-phase lock-in demodulation

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

Signed baseband recovery requires phase information.

### Options considered

Magnitude only; X/Y coherent recovery.

### Decision

Reference the lock-in to the selected carrier source and record X and Y plus settings and overload state.

### Rationale

Magnitude removes polarity, while calibrated X/Y rotation preserves it.

### Consequences

Phase and ultrasound-only offset calibrations are mandatory.

### Verification required

Sideband injection, phase, drift, rate, filter, and overload tests.

## DDR-007: Require acoustic-blocking and dummy-load controls

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

RF pickup and nonlinear electronics can mimic sidebands.

### Options considered

Combined condition alone; complete artefact-control matrix.

### Decision

Require acoustic blocking and dummy load alongside baseline, source-only, ultrasound-only, polarity, displacement, and frequency controls.

### Rationale

Causality cannot be assigned from a carrier-band signal alone.

### Consequences

Incomplete control sets cannot support a candidate AE conclusion.

### Verification required

Predefined reductions, phase relationships, spatial dependence, and repetition.

## DDR-008: Validate electronics before skull work

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

Skull complexity can conceal electronic faults and artefacts.

### Options considered

Immediate skull experiment; phased electronic/source/receiver/saline validation.

### Decision

Complete electronic and saline acceptance before skull experiments.

### Rationale

Staged tests isolate failure modes.

### Consequences

Skull protocols remain pending earlier acceptance.

### Verification required

Phase-gate evidence and review.

## DDR-009: Restrict current work to non-living materials

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

The platform is early-stage and safety is unvalidated.

### Options considered

Phantom/ex-vivo research only; biological testing.

### Decision

Restrict all current work to saline, synthetic phantoms/skulls, and controlled ex-vivo material.

### Rationale

Hardware, mechanism, exposure, and safety are unvalidated.

### Consequences

No person or animal use and no clinical claims.

### Verification required

Qualified independent review would be required before any future scope change.

## DDR-010: Evaluate higher-frequency configurations

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

Frequency affects focus, transmission, heating, and artefacts.

### Options considered

Baseline only; separately calibrated higher-frequency candidates.

### Decision

Retain 650 kHz, 750 kHz, approximately 1 MHz, and custom candidates.

### Rationale

Their system-level trade-offs require measurement rather than assumption.

### Consequences

The roadmap includes staged comparison after baseline acceptance.

### Verification required

Complete carrier-specific electrical, acoustic, thermal, and localisation evidence.

## DDR-011: Do not assume a universal transducer

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

A nominal frequency or bandwidth claim does not establish loaded performance.

### Options considered

Reuse by assumption; reuse only after per-frequency validation.

### Decision

Do not assume one narrowband or broadband transducer covers every frequency.

### Rationale

Impedance, field, phase, power, and temperature are configuration dependent.

### Consequences

Shared hardware still needs a complete calibration record per carrier.

### Verification required

Per-frequency impedance, power, hydrophone, field, and thermal tests.

## DDR-012: Keep active source electronics outside

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

Internal active electronics introduce uncontrolled RF and electrical paths.

### Options considered

Internal powered oscillator; externally driven passive electrodes.

### Decision

Keep oscillator, isolation, power, current source, and sensing electronics external.

### Rationale

This reduces internal artefact sources and keeps current measurable.

### Consequences

A documented sealed feedthrough and cable path are required.

### Verification required

Leakage, isolation, feedthrough, cable, and dummy-load tests.

## DDR-013: Prohibit a shared source return initially

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

A shared return makes current paths and source separation ambiguous.

### Options considered

Shared return; independent bipolar pairs.

### Decision

Use an independent bipolar pair for every source.

### Rationale

Known closed current paths improve interpretability.

### Consequences

Multi-source arrays require additional conductors and calibrations.

### Verification required

Measure channel isolation, individual currents, and source-only leakage.

## DDR-014: Preserve raw X and Y channels

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

Lock-in magnitude discards sign and can conceal phase changes.

### Options considered

Record R only; stream X/Y and derive R and signed voltage reproducibly.

### Decision

Always record X and Y with range, filter, rate, reference, and overload metadata.

### Rationale

Raw quadratures support offset correction, phase rotation, polarity, and drift review.

### Consequences

Storage and acquisition must support dual-channel streaming.

### Verification required

Electronic phase, polarity, rate, filter, and overload tests.

## DDR-015: Complete electronic validation before skull experiments

- Date: TBD
- Status: Accepted
- Decision owner: TBD
- Related issue: TBD
- Related commit: TBD

### Context

Complex acoustic material should not be used to debug an unverified receiver chain.

### Options considered

Begin with skull experiments; pass electronic and saline gates first.

### Decision

Require validated loopback, source, receiver, and saline controls before skull work.

### Rationale

Sequential gates isolate faults and artefacts.

### Consequences

Skull work remains explicitly not started.

### Verification required

Reviewed phase acceptance records for phases 1–4.

