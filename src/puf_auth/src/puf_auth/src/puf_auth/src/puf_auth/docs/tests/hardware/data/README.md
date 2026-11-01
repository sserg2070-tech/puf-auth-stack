# PUF Authentication Stack

Open reference stack for PUF-rooted authentication designed for **low-bandwidth, intermittently connected sensor networks**.

This project is being developed as part of a proposal to the [NLnet Restack](https://nlnet.nl/restack/) programme.

## Goal

Provide a complete, usable and fully open implementation of PUF-based authentication that works under the constraints of:

- Very low data rates (tens of bits per second)
- Long offline periods
- Resource-constrained sensor nodes (environmental buoys, gliders, remote stations)

## Planned components

- Specification and reference library
  - Code-offset fuzzy extractor
  - Hash-chain token scheme (Lamport/TESLA-style)
  - Signed revocation lists
  - Authenticated commands
  - Test vectors
- Simulation harness (link-budget and temperature-noise models)
- Open-hardware readout rig
- Public measurement dataset from commercial SAW devices

## Current status

Repository skeleton and initial module structure created.  
Core implementation will be developed during the project.

## Background

Architectural foundation (open access):  
[https://doi.org/10.5281/zenodo.21890904](https://doi.org/10.5281/zenodo.21890904)

## Licence

- Software: [Apache-2.0](LICENSE)
- Hardware: CERN-OHL-S
- Documentation and data: CC-BY

## Author

Skrebtsov Sergiy  
Independent researcher, Sweden
