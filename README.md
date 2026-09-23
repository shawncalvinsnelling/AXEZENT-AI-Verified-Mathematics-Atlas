# Axezent AI Verified Mathematics Atlas

![AXEZENT AI Logo](assets/axezent-ai-logo.svg)

Truth-first verified mathematics artifacts and public AXEZENT research software.

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

## AXEZENT commercial platform

[AXEZENT Commercial Software Suite](commercial/axezent-commercial-suite/) contains the customer-facing product portfolio, pricing, enterprise information, onboarding, and public evaluation site.

## Research paper

[Six-Cycle Insertion and Hook-Unimodality in Higher Lie Characters](papers/six-cycle-hook-unimodality-2026/)

## Truth boundary

This atlas distinguishes exact verified artifacts from preview systems and open mathematical problems. It does not claim global OPAC-018 closure or solutions to major open problems unless a complete evidence record establishes that status.
