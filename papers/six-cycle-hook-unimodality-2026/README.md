# Six-Cycle Hook-Unimodality — referee-candidate v2 branch

**Author:** Shawn Calvin Snelling  
**ORCID:** 0009-0009-3605-7109  
**Original public preprint date:** 22 September 2026  
**v2 referee-candidate date:** 24 September 2026  
**Status:** revision branch for independent review; not journal accepted

## Why v2 exists

Editorial feedback identified two screening questions: significance of the partial result and mathematical novelty/structure of the proof. The v2 audit keeps the original all-s unimodality theorem and adds a stronger exact statement for the exceptional six-cycle family:

M_(6^s)(x) is strictly log-concave on its nonzero support if and only if s >= 7.

The threshold is proved symbolically. It is not inferred from finite testing.

## Main results in the candidate revision

1. M_(6^s)(x) is unimodal for every s >= 1.
2. (1+x)M_(6^s)(x) is strictly log-concave on its nonzero support for every s >= 1.
3. M_(6^s)(x) itself is strictly log-concave exactly for s >= 7.
4. If nu is nonempty, contains no six, and M_nu(x) is unimodal, then M_(nu union (6^s))(x) is unimodal for every s >= 1.
5. Every nonempty partition with parts in {1,2,3,4,5,6} has a unimodal hook-multiplicity sequence.

## Files

- Original v1 source: Snelling_Six_Cycle_Hook_Unimodality_2026-09-22.tex
- Referee-candidate v2 source: Snelling_Six_Cycle_Hook_Unimodality_2026-09-24_v2.tex
- Experimental chronology: EXPERIMENTAL_DISCOVERY_LOG.md
- Referee audit: REFEREE_AUDIT_V2.md
- Symbolic threshold audit: verification/symbolic_threshold_audit.py
- Independent AHR reconstruction: ../../axezent_ai_verified_math/six_cycle_v2.py
- Adversarial tests: ../../tests/test_six_cycle_v2.py

## Independent reconstruction

The v2 verifier starts from the published AHR r=6 product identity, reconstructs the y^s coefficient over the integers, divides exactly by 1+x, and compares the resulting P_s with the manuscript's closed coefficient formula.

This is intentionally independent of the legacy closed-form evaluator.

## Truth boundary

- The all-s claims are mathematical claims supported by symbolic proofs.
- Finite regression tests are reproducibility/adversarial checks, not proofs of an infinite statement.
- The discrete convolution lemma is classical strong unimodality and is now attributed to Keilson--Gerber (1971).
- Historical priority of the exact s=7 threshold remains subject to a complete specialist literature review.
- The original DOI is a public preprint record; v2 should receive updated archival metadata only after the revision is frozen.
