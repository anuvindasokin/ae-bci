# Data Management

- Never modify raw data; treat it as read-only.
- Processed data must reference raw data and the processing commit.
- Every dataset includes validated metadata and the acquisition Git commit.
- Do not place large raw files in normal Git history; use Git LFS or approved object storage.
- Label synthetic datasets and keep measurements separate from simulations.
- Retain raw data for excluded runs and document every exclusion reason.
- Never alter results manually for appearance.
- Do not commit personal, clinical, or identifiable data.
- Calibration records identify instrument, serial, status, and date.
- Every figure must be reproducible from a versioned script.
- Record hashes for released datasets and do not silently modify data.

