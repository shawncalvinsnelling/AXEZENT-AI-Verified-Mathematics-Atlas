# AXEZENT Riemann Hypothesis — Certificate Research & Open Review

**Shawn Calvin Snelling · Version 0.1.0 · 12 October 2026**

**Status: public research for technical review. This is not a complete proof of RH, a journal acceptance, or a Millennium Prize application.**

This project makes a specific result reproducible: without assuming RH, an integer-interval program certifies

$$
|\psi(x)-x|\le\frac1{16}\sqrt{x}(\log x)^2
\quad\text{for every real }x\in[256,1{,}048{,}576],
$$

where $\psi(x)=\sum_{p^k\le x}\log p$. The manuscript also gives standard conditional implications to RH and identifies the unproved all-scale input. No worldwide novelty or numerical record is claimed.

## Start here

[Mathematical note](MATHEMATICAL_NOTE.md) · [Exact claim ledger](CLAIMS.json) · [Reviewer guide](REVIEW_GUIDE.md) · [Recorded finite receipt](receipts/finite_envelope_receipt.json) · [Preparation and provenance](PROVENANCE.md)

The mathematical note distinguishes a proved implication from its unproved hypothesis. Neither an efficient verifier nor a finite test range supplies the missing hypothesis.

## Reproduce from a clean copy

Python 3.11 or newer; standard library only. No paid service, API key, AI subscription, or third-party Python package is needed for this module.

From the Atlas repository root:

```text
cd research/riemann-hypothesis
python check_integrity.py
python replay.py
```

On Windows, `py -3 replay.py` is an alternative when Python is registered with the launcher. `replay.py` runs the 17 targeted tests, regenerates the full finite certificate normally and with `python -O`, and compares both with the frozen receipt. It exits nonzero on failure and writes logs to `_replay/`.

Expected final marker:

```text
PASS_RH_FINITE_REPLAY_NOT_RH_PROOF
```

Expected finite scope: 82,197 constant-psi intervals, the final endpoint, 82,025 primes and 82,267 prime-power events through the cutoff. The ordered exact-cell SHA-256 is `ee5b85b29884d7071c0471f05b38b4f468e7beb36d3ae9efde14fdf0eb09f744`.

The hash checks consistency, not mathematical truth. Review the enumeration, interval arithmetic, and written coverage argument as well as running the code.

## What is proved, conditional, and open?

| ID | Statement | Status |
|---|---|---|
| RH-FINITE-001 | The displayed envelope for all real x in the specified finite interval | Computer-assisted finite-domain result; reproduction supplied |
| RH-IMPL-001 | A fixed-degree polynomial bound on the normalized error at every sufficiently large scale implies RH | Standard conditional implication; hypothesis unproved here |
| RH-IMPL-002 | A uniform signed dyadic error bound supplies a sufficient global envelope | Conditional transfer; hypothesis unproved here |
| RH-OBSTRUCTION-001 | Termwise absolute values cannot give the proposed square-root dyadic estimate | Elementary proved limitation of that route |
| RH-OPEN-001 | Establish a sufficient all-scale bound for the actual prime error | Open; no certificate supplied |

No Lean, Coq, or Isabelle kernel certificate is included. The human-readable unbounded implications require mathematical review; the Python code verifies the finite claim only.

## Review and corrections

Use the publication pull request for line-specific review, or open a repository issue headed `[RH review]` or `[RH reproduction]`. Include the commit, claim ID, exact location, and argument or reproducible failure. See the [reviewer guide](REVIEW_GUIDE.md). Corrections and negative results are welcome. A successful software run is not specialist approval of the full mathematical argument.

AHR higher-Lie results and OPAC are separate projects, not assumed premises for RH. This module does not change their manuscripts or claims.

## The Millennium Prize is the research goal, not a status badge

The target is the actual [Riemann Hypothesis](https://www.claymath.org/millennium/riemann-hypothesis/). Under the [Clay Mathematics Institute rules](https://www.claymath.org/millennium-problems/rules/), consideration requires publication in a Qualifying Outlet, at least two years after publication, and general acceptance in the global mathematics community. CMI does not accept direct submissions. A GitHub upload does not by itself satisfy these conditions or start a prize clock.

## Attribution and permissions

Prepared for Shawn Calvin Snelling / AXEZENT with ChatGPT-assisted mathematical exposition and code preparation. Cite the exact commit and the [module citation](CITATION.cff). Known identities and implications are attributed in the note; no fictional reviewer endorsements are used.

The existing [Atlas licensing notice](../../LICENSE.md) is unchanged. These scripts are presented as public evaluation tools under its stated research-evaluation permission; this publication does not grant a new general open-source license. No payment is required to inspect this public work or execute the supplied evaluation copy.
