# AXEZENT RH — A–Z research record and route inventory

**Shawn Calvin Snelling · public record prepared 18 October 2026**

This document identifies the recovered A–Z RH research program, distinguishes its earlier saved records from its public GitHub history, and publishes its broader route inventory for technical comparison. It is a research record, not a claim that every possible theorem or proof has been enumerated or that RH has been solved.

## The framework and its RH entry

- **Framework:** Artificial Intelligence v7 MONOLITH — A–Z Hybrid Completion Scan.
- **Target registry:** Open Mathematics 1000, entry **OM1000-0001: Riemann Hypothesis**.
- **Specific recovered scan:** **G0362**, headed 27 September 2026, 22:35 CDT.
- **Broader RH collection:** **AXEZENT RH — Fringe-to-Rigorous Master Atlas V3**.
- **Definition & Meaning Hypergraph:** stores mathematical objects, definitions, dependencies, source references, and proof-status information. Such coverage identifies possible connections; it does not automatically establish a new result using those objects.

The recovered 1,000-target registry is a finite research catalogue. Its size is not a count of solved problems. The V3 atlas contains 80 numbered research routes and eight proposed combinations, reproduced below. These are research routes, standard criteria, tools, and speculative directions, not 80 new theorems.

## Dated evidence

| Date | Record | What the evidence establishes |
|---|---|---|
| 27 September 2026, 22:35 CDT | Date in the G0362 report heading | The report identifies this research cycle and records RH as OPEN. |
| 28 September 2026, 03:41:50 UTC | Saved-file creation metadata for that G0362 report | An earlier saved research record exists. This is not evidence that it was already public on GitHub. |
| 6 October 2026 | [OpenAI release announcement](https://openai.com/index/sharing-ai-progress-in-mathematics/) | Publication date of the release discussed below. |
| 12 October 2026, 17:33:27 UTC | [AXEZENT commit 51ae37f6c4b2e94c559cfe341bf2a6f4f786badf](https://github.com/shawncalvinsnelling/AXEZENT-AI-Verified-Mathematics-Atlas/commit/51ae37f6c4b2e94c559cfe341bf2a6f4f786badf) | Git commit date for the scoped public RH certificate module. |
| 12 October 2026, 17:34:33 UTC | [Public review PR #9](https://github.com/shawncalvinsnelling/AXEZENT-AI-Verified-Mathematics-Atlas/pull/9) | GitHub's PR creation record for the public review package. The PR remained open and unmerged when this document was prepared. |
| 13 October 2026, 22:35:10 UTC | Saved-file creation metadata for `AXEZENT_RH_FRINGE_ATLAS_V3.zip` | Date of the recovered V3 package; this version postdates OpenAI's October 6 release. |
| 18 October 2026 | This research record | New public documentation of the recovered scan and broader route inventory. Its publication date must not be substituted for, or backdated to, an earlier saved-file date. |

The existing public RH certificate module therefore does not establish GitHub publication before OpenAI's October 6 release. Earlier saved research is a separate category of evidence. Historical priority for a specific new result would require matching its exact statement, hypotheses, argument, and dated source, together with a review of earlier literature. Shared terminology or an entry in a broad catalogue does not establish that match.

## What G0362 recorded

Source: `Artificial_Intelligence_v7_Hourly_Report_20260927_2235_CDT.md`. The following is a mathematical summary of that saved report; unrelated material is omitted.

The scan explored a centered divisor polynomial

\[
D_a(t)=\sum_{r\mid a}\exp\left(it(\log r-\tfrac12\log a)\right)
\]

and the Euler-product factorization

\[
F(s,t)=\sum_{a\ge1}\frac{\mu(a)D_a(t)}{a^s}
=\frac{H(s,t)}{\zeta(s+it/2)\zeta(s-it/2)}.
\]

For real t, the Dirichlet series identity is initially interpreted in its absolute-convergence half-plane Re(s)>1. The report describes the correction product H as absolutely convergent for Re(s)>1/2. This does not make the reciprocal zeta factors zero-free in that larger region.

The same scan recorded:

- square-part normalization `X_b=Y/b^2`, `R_b=z/b`, and `R_b^2=B X_b log Y` under `z^2=B Y log Y`;
- the normalized window identity `log(R_b^2/a)=log(B log Y/x)` for `a=X_b x`;
- a shared residual `R_z(s)=1-zeta(s)M_z(s)` linking the investigated Heath-Brown approximation to a Nyman–Beurling/Báez-Duarte research route;
- a sign-placement obstruction to directly importing the examined divisor-window estimates;
- a remaining coupled signed-cancellation estimate over the scale and Fourier variables.

The report records finite Python and C++ checks and no formal theorem-prover run. Those historical executions have not been independently reproduced as part of preparing this publication. Its own parent conclusion is **RH remains OPEN**. This document does not promote historical status labels into a new mathematical certification or novelty claim.

## Current public mathematical contribution

The existing [mathematical note](MATHEMATICAL_NOTE.md), [claim ledger](CLAIMS.json), and [finite receipt](receipts/finite_envelope_receipt.json) document

\[
|\psi(x)-x|\le\frac1{16}\sqrt{x}(\log x)^2
\quad\text{for every real }256\le x\le1{,}048{,}576,
\qquad \psi(x)=\sum_{p^k\le x}\log p.
\]

This is a finite-domain certificate with integer interval arithmetic. The conditional all-scale implications and the unproved all-scale input are stated separately. See the existing [review guide](REVIEW_GUIDE.md) for reproduction and mathematical objections.

The broader research targets include signed Möbius cancellation, Weil-form positivity, matrix domination, and Jensen hyperbolicity. Each requires its own exact hypotheses and missing estimates. In particular, strict log-concavity of a general positive sequence is insufficient to establish every Jensen hyperbolicity condition.

## Comparison with the October 2026 OpenAI release

OpenAI's [current repository README](https://github.com/openai/math/blob/main/README.md), inspected on 18 October, lists **719 manuscripts in 372 result families** and says that their verification stages differ. That current count differs from the 722 manuscripts reported at the initial release.

The relevant [family 003 preprint](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/README.md) is titled *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s)>7/8*, with a manuscript date of 30 September. OpenAI's [overview](https://github.com/openai/math/blob/main/overview.tex) describes a zero-free half-plane for Dirichlet L-functions and a companion 11/12 argument. This document reports those claims; it does not certify the full preprints or Lean formalizations.

| Comparison | AXEZENT record | OpenAI family 003 |
|---|---|---|
| Mathematical neighborhood | Prime error, Möbius sums, shifted zeta factors, positivity and spectral routes | Claimed global zero-free half-plane |
| Explicit established scope in AXEZENT's public certificate | Real x in a specified finite interval | Claimed Re(s)>7/8, an unbounded complex region |
| Full RH | Remains an open target in this project | A 7/8 bound alone does not establish RH's critical line Re(s)=1/2 |
| Demonstrated identity of results or proofs | Not established by this inspection | Requires an exact theorem-and-proof comparison |

A future comparison should map precise objects and hypotheses, cite the first dated occurrence of the actual argument, and distinguish standard background from each work's specific contribution. The inspected records establish earlier AXEZENT research on related subjects; they do not establish that AXEZENT already had the particular 7/8 theorem or its proof.

## Publication scope

Prepared with ChatGPT assistance for Shawn Calvin Snelling. Existing licensing and citation terms remain unchanged. The original finite verifier, receipt, mathematical note, and manifest are unchanged. The addition is a dated documentation file. The V3 text below is reproduced as historical research planning; its closure conditions remain obligations.

## Recovered V3 route inventory

The following text is reproduced from `MASTER_FRINGE_ATLAS.md` inside the saved V3 archive. Its original warning about nonexhaustiveness is retained.

---

# AXEZENT RH — Fringe-to-Rigorous Master Atlas V3

Researcher: Shawn Calvin Snelling
Project: AXEZENT-Riemann-Hypothesis

This is a maximal research atlas, not a claim that literally every conceivable proof idea has been enumerated.

## Rule 0 — Fringe-to-rigorous conversion

Every idea must become at least one of:
- an exact identity,
- a uniform inequality,
- a convergence theorem,
- a positivity statement,
- a spectral statement,
- a finite certificate plus a proved finite-to-infinite bridge,
- or a counterexample/falsification test.

No metaphor closes RH by itself.

## I. Established RH-equivalent attack surfaces

1. Chebyshev prime-error route: psi(x)=x+O(x^(1/2+eps)) for every eps>0.
2. Prime-counting route: RH-equivalent bounds for pi(x)-li(x).
3. Mertens/Mobius route: square-root-scale cancellation of M(x).
4. Weil positivity route: positivity of the explicit-formula quadratic form.
5. Li coefficients: lambda_n >= 0 for all n.
6. Nyman-Beurling / Baez-Duarte: Hilbert-space density/approximation.
7. Robin/Lagarias divisor inequalities.
8. Jensen/Polya hyperbolicity.
9. de Bruijn-Newman flow.
10. Hilbert-Polya self-adjoint spectral operator.
11. de Branges / canonical systems.
12. Argument principle / zero-count route.

## II. Explicit-formula / analytic routes

13. Smoothed explicit-formula signed cancellation.
14. Dirichlet-polynomial large-value route.
15. Zero-density bootstrap.
16. Density plus zero-repulsion.
17. Mollifier closure.
18. Moment hierarchy.
19. Pair-correlation rigidity.
20. Short-interval prime rigidity.

## III. Recovered AXEZENT / Snelling routes

21. Prime Resonance Collapse — must be phase-sensitive and tied to the explicit formula.
22. Snelling Harmonic Matrix Collapse — spectral invariant route; must avoid prior rank-one information loss.
23. Many-to-One Phase-Displacement Collapse — compress many frequencies into exact moment kernels.
24. Mobius diagonal/off-diagonal law: C_N = D_N + O_N; target uniform off-diagonal domination.
25. AXEZENT Matrix Compression Trick: H_m = D_m + R_m with lambda_min(D_m) > ||R_m||_op.
26. Certified Retention Invariant — prune blocks without losing a worst-case witness.
27. Monotone Energy Decoder Invariance — preserve extrema under justified monotone transforms.
28. Objective-Dependency Gate — every RH spectral object must actually encode zeta/prime information.
29. Defect-Boundary Verification — positive middle + exact boundaries + finite base.
30. Polynomial Identity Certificates — only after a real degree bound is proved.
31. Kronecker/Radix Packing — exact certificate acceleration only.
32. Tail-Defect Rewrite philosophy — split automatic regions from dangerous regions.
33. Green-Schur / Schur-complement induction — possible PSD propagation.
34. Finite-type M-matrix analogy — speculative unless exact sign structure exists.
35. ReceiptRail deterministic replay.
36. ATRM canonicalization of candidate lemmas into finite obligations.
37. CSL typed implication graph to stop circular reasoning.

## IV. Spectral / operator / geometry routes

38. Regularized determinant route: xi(s) as a determinant of a self-adjoint/Hilbert-Schmidt operator.
39. Trace-formula route with primes as periodic-orbit data and zeros as spectral data.
40. Quantum-graph route.
41. Berry-Keating / scaling Hamiltonian route.
42. Positive-kernel route.
43. Inverse spectral reconstruction.
44. Noncommutative geometry / adelic trace route.

## V. Entire-function / complex-analysis routes

45. Laguerre-Polya closure.
46. Wronskian hierarchy.
47. Horizontal monotonicity of |zeta(s)|.
48. Rouche approximation tower.
49. Conformal/extremal quadratic-form route.
50. Phragmen-Lindelof barrier route.

## VI. Harmonic / signal-processing routes

51. Fejer PSD kernel tower.
52. Wavelet multiresolution for prime error.
53. Hardy/Carleson embedding.
54. Phase-retrieval route.
55. Uncertainty-principle route.
56. Perfect-reconstruction filter-bank route.

## VII. Probability / dynamics / information routes

57. Martingale prime-error decomposition.
58. Renormalization fixed point for normalized prime-error profiles.
59. Lyapunov barrier.
60. Entropy / relative-entropy formulation.
61. Information-theoretic uncertainty.
62. Optimal-transport formulation.
63. Large-deviation rigidity.

## VIII. Algebraic / certificate / proof-complexity routes

64. Sum-of-squares positivity.
65. Semidefinite hierarchy with exact rational dual certificates.
66. Nullstellensatz contradiction after a rigorous finite reduction.
67. Groebner/elimination route.
68. Total-positivity / PF hierarchy, with explicit failure checks.
69. Hankel determinant hierarchy.
70. Toeplitz/Herglotz positive-definite sequence route.

## IX. Topological / fringe-but-testable routes

71. Fredholm/index-theorem route.
72. Winding-number invariant.
73. Persistent-homology discovery route, requiring a later theorem.
74. Category/functor route from arithmetic to spectral objects.
75. Typed hypergraph parent object for cross-route invariants.
76. Dual-certificate minimax game.
77. Robust-control / Nyquist / KYP route.
78. Passivity / positive-real transfer-function route.
79. Scattering-theory route.
80. Supersymmetric factorization H=A* A tied to an exact xi determinant.

## X. Highest-value cross-combinations

A. Weil + Mobius + matrix domination:
Mobius split -> H_m=D_m+R_m -> diagonal margin > off-diagonal norm -> Weil positivity -> RH.

B. Explicit formula + wavelets + Carleson:
prime error -> dyadic coefficients -> square-function bound -> RH-scale error.

C. Rouche + finite certificates + entire approximants:
all approximants have line zeros + uniform boundary error -> zero-count transfer.

D. Jensen + determinant certificates + Schur induction:
uniform determinant positivity -> hyperbolicity.

E. Nyman-Beurling + exact Gram matrices + retention invariant:
finite approximation + certified obstruction pruning -> density theorem.

F. Li + Toeplitz/Hankel + SOS:
positive-moment representation -> all Li coefficients nonnegative.

G. Connes-style finite Weil approximants + AXEZENT convergence certificates:
prove finite-to-infinite convergence rather than merely finite zero alignment.

H. Dirichlet-polynomial large values + AXEZENT defect bootstrap:
turn a zero-density exponent improvement into a contracting map toward 1/2.

## XI. Recovered blockers that must remain visible

1. Phase-blind observables are insufficient.
2. Finite prime-phase signals have approximate recurrences; resonance is not unique.
3. A raw prime-log Hamiltonian can have the wrong spectral counting law.
4. Rank-one CSL Gram matrices lose information.
5. Objective-independent matrices cannot recover arbitrary objectives.
6. Finite-height zero verification does not imply global RH.
7. Absolute-value bounds destroy the signed cancellation needed at RH scale.
8. Runtime complexity does not bound arithmetic error magnitude.
9. Functional-equation symmetry alone does not force zeros to the critical line.
10. A smooth weight does not create cancellation without a theorem.
11. PIT needs a proved degree bound first.
12. Finite PSD matrices need density, continuity, and uniform control before implying infinite-dimensional positivity.

## XII. Research priority

Tier 1:
- Weil + Mobius + matrix domination
- finite Weil approximants + convergence
- explicit-formula signed cancellation + wavelet/Carleson control
- Rouche approximation tower
- Jensen/Wronskian hierarchy

Tier 2:
- Li positivity
- Nyman-Beurling
- Robin/Lagarias
- Mobius/Mertens growth
- de Bruijn-Newman

Tier 3:
- Hilbert-Polya
- trace formula / quantum graph
- noncommutative geometry
- robust-control/passivity realization
- renormalization/Lyapunov
- topological index/winding

Tier 4 discovery-only until formalized:
- prime-resonance visualizations
- entropy heuristics
- phase manifolds
- speculative time/field analogies

## XIII. Closure standard

RH should be claimed only when one route has:
1. a complete theorem statement,
2. every assumption explicit,
3. no RH-equivalent hypothesis imported,
4. a universal proof covering the infinite domain,
5. all limit/interchange steps justified,
6. independent reproduction,
7. adversarial counterexample audit,
8. translation into a standard RH-equivalent formulation,
9. and a referee-readable proof independent of AXEZENT terminology.

Until then: active research, not failure.


## Source fingerprints

- Original V3 archive SHA-256: `2c70ac0e541a0757c76f46c461f19699e2a540c7d84d9cd58c1db26f3d72bd53`.
- Original `MASTER_FRINGE_ATLAS.md` SHA-256: `89ba9aeb2ba727daa9e2ac7246044d908ce4858a83db3d49ddfcc7e430ff6819`.
- These fingerprints identify the inspected source bytes. Hashes alone establish neither an earlier publication date nor mathematical truth.
