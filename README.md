# Axezent AI Verified Mathematics Atlas

![AXEZENT AI Logo](assets/axezent-ai-logo.svg)

Truth-first scoped verification artifacts and public AXEZENT research software.

**Researcher:** Shawn Calvin Snelling · [ORCID 0009-0009-3605-7109](https://orcid.org/0009-0009-3605-7109)

## Public research

This atlas organizes finite certificates, exact receipts, tests, truth ledgers, Lean gates, and the public six-cycle hook-unimodality preprint.

## Available software

### Six-Cycle Exact Certifier

Generate an exact verification receipt for the published family `(6^s)`:

```bash
python -m axezent_ai_verified_math.cli 6 --json
```

or, after package installation:

```bash
axezent-six-cycle 6 --json
```

The CI regression suite checks the published formulas and properties for `s=1..250`.

The certifier's output is limited to the stated formulas, inputs, and checks. It is not independent peer review or a representation that the full arbitrary-partition conjecture is solved.

## AXEZENT commercial platform

[AXEZENT Commercial Software Suite](commercial/axezent-commercial-suite/) contains the customer-facing product portfolio, preview pricing, enterprise information, onboarding, legal terms, privacy information, and public evaluation site.

General public paid checkout is not enabled from this repository. See the [Launch Status](commercial/axezent-commercial-suite/LAUNCH_STATUS.md).

## Research paper

[Six-Cycle Insertion and Hook-Unimodality in Higher Lie Characters](papers/six-cycle-hook-unimodality-2026/) · DOI [10.5281/zenodo.22910548](https://doi.org/10.5281/zenodo.22910548)

## Truth boundary

This atlas distinguishes exact verified artifacts from preview systems and open mathematical problems. It does not claim global OPAC-018 closure or solutions to major open problems unless a complete evidence record establishes that status.

## Licensing

This repository uses a mixed-rights model. The six-cycle paper is CC BY 4.0; software and other materials may have different rights.

See [LICENSE.md](LICENSE.md) and the [AXEZENT license map](commercial/axezent-commercial-suite/LICENSE_AND_ATTRIBUTION.md).
