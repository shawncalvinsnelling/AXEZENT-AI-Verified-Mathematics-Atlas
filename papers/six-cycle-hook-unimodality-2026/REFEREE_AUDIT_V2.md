# Referee Audit v2 — Six-Cycle Hook-Unimodality

**Date:** 24 September 2026  
**Purpose:** hostile-referee checklist before any journal re-delivery  
**External communication:** none sent by this audit

## A. Source-identity gate

**Target:** Reproduce the r=6 AHR generating function and coefficients without assuming the final closed formula.

**Status:** PASS for the implemented finite-instance reproducer.

The independent route expands the published r=6 product exactly over integer coefficient dictionaries, extracts the y^s coefficient, divides exactly by 1+x, removes the forced shift x^(2s-1), and compares the result with the closed q_(s,k) formulas.

**Truth boundary:** finite reconstruction supports the symbolic derivation but does not replace the all-s proof.

## B. Unimodality gate

**Target:** prove P_s rises and then falls for every s>=1.

**Status:** PASS in the manuscript proof.

Special cases s=1,2 are explicit. For s>=3, the initial differences are positive, the cubic-range forward difference is a convex quadratic, and the terminal differences are negative. The sign pattern therefore changes at most once.

## C. Raw strict-log-concavity threshold

**Claim:** P_s is strictly log-concave if and only if s>=7.

**Status:** PASS algebraically, subject to ordinary peer review.

### Failure side

- s=1: P_1=(1,2,1,1), giving an internal determinant -1.
- For s=2,...,6, the controlling determinant is

  Delta_(s,2) = (s^4 - 8s^3 + 13s^2 - 6s - 12)/4,

  taking values -5, -12, -21, -23, -3.

### Positive side

For s>=7, with u=s-7,

Delta_(s,2) = u^4/4 + 5u^3 + 139u^2/4 + 93u + 60 > 0.

All remaining determinant families have explicit positive-coefficient certificates in the manuscript and symbolic audit.

## D. Smoothed strict log-concavity

**Claim:** (1+x)P_s is strictly log-concave for every s>=1.

**Status:** PASS in the current symbolic certificate chain.

The wording was tightened: positive endpoints alone do not establish contiguous support. Nonnegative hook multiplicities plus strict internal determinant inequalities and positive endpoints rule out an internal zero.

## E. Convolution / insertion gate

**Status:** PASS with attribution correction.

The preservation of unimodality under convolution with a log-concave no-internal-zero sequence is classical discrete strong unimodality. The revision cites Keilson--Gerber (1971) and retains a self-contained finite proof.

**Novelty boundary:** this classical lemma is not presented as a new theorem.

## F. Parts-at-most-six closure

**Status:** PASS with expanded proof.

The revision explicitly separates monomial factors for part sizes 1,2,3; the single 1+x factor structure for size 4; the one nontrivial unimodal bracket for size 5; and the binomial/log-concave smoothing created by disjoint-size assembly. Sixes are then inserted with the six-cycle insertion theorem.

## G. Novelty / literature gate

**Status:** OPEN, not failed.

Current targeted searches recover AHR's 2023 paper and its explicit exclusion of r=6 from Conjecture 8.2, but have not yet located a publication stating the exact s=7 threshold. Absence from a targeted search is not proof of historical priority.

Before a priority claim is made, search MathSciNet, zbMATH, arXiv forward citations of AHR, Google Scholar, post-2023 higher-Lie literature, and hook-multiplicity log-concavity literature.

## H. Journal-facing significance gate

The revision should be evaluated on these concrete contributions rather than on the classical convolution lemma:

1. exact all-s coefficient structure for the exceptional r=6 family;
2. all-s unimodality;
3. exact raw strict-log-concavity threshold s=7;
4. one-factor smoothing restoring strict log-concavity for all s;
5. insertion/closure producing an unbounded nonrectangular family.

## I. Robbins Prize preparation gate

**Status:** NOT YET A PRIZE-SUBMISSION STAGE.

The AMS correspondence indicates that peer-reviewed publication comes first and that the significance of the experimental component is for the selection committee.

Preserve the actual chronology: exact finite scans suggested s=7, then symbolic algebra closed the all-s theorem. Do not rewrite the chronology after the fact.

## J. Release gate

Do not re-deliver to the editor until all of the following are green:

- [x] v1 preserved
- [x] v2 theorem statement drafted
- [x] exact threshold proof drafted
- [x] classical strong-unimodality attribution added
- [x] parts-<=6 proof expanded
- [x] independent AHR reproducer added
- [x] adversarial threshold tests added
- [x] discovery log added
- [x] CI runs v2 tests and symbolic audit
- [x] v2 PDF builds cleanly
- [ ] complete specialist literature audit
- [ ] at least one independent human mathematical attack
- [ ] final author line-by-line proof check
- [ ] archival DOI/version metadata updated after freeze


## K. Automated gate receipts

- Atlas Verification run: SUCCESS on the referee-v2 branch.
- Six-cycle v2 two-pass LaTeX build: SUCCESS on the referee-v2 branch.
- These automated passes verify the implemented checks and build reproducibility; they are not substitutes for independent peer review.
