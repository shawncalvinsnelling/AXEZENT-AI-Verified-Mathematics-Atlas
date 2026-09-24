# Experimental discovery and verification log

## Scope

This file records the chronology of the six-cycle hook-multiplicity project.
It is an evidence log, not a claim of journal acceptance or historical priority.

## 2026-09-22 — public v1 preprint

The first public manuscript stated and proved:

1. (M_{(6^s)}(x)) is unimodal for every integer (s\ge 1).
2. ((1+x)M_{(6^s)}(x)) is strictly log-concave on its nonzero support.
3. Six-cycle insertion preserves unimodality when the remainder is unimodal
   and has no part of size six.
4. Every nonempty partition with parts in ({1,2,3,4,5,6}) has a unimodal
   hook-multiplicity sequence.

The proof was symbolic for all (s); finite computation was an audit layer.

## 2026-09-23 — editorial feedback

Akihiro Munemasa, editor-in-chief of *Algebraic Combinatorics*, replied to the
submission inquiry.  He identified two initial-screen questions:

- Is the partial result a significant contribution?
- Is the proof technique novel / mathematically interesting enough?

No acceptance, referee validation, or endorsement of correctness was implied.

## 2026-09-24 — stronger threshold found during adversarial audit

A post-feedback audit tested the unsmoothed coefficient sequence of
(P_s(x)), where
(M_{(6^s)}(x)=x^{2s-1}P_s(x)).

Exact determinant scans suggested a sharp transition:

- raw strict log-concavity fails for (s=1,dots,6);
- raw strict log-concavity holds from (s=7) onward.

The scan was then replaced by a symbolic proof.  The controlling early
determinant is

[
\Delta_{s,2}
= q_{s,2}^2-q_{s,1}q_{s,3}
= \frac{s^4-8s^3+13s^2-6s-12}{4}.
]

It is negative for (s=2,dots,6), and with (u=s-7\ge0),

[
\Delta_{s,2}
= \frac14u^4+5u^3+\frac{139}{4}u^2+93u+60>0.
]

The remaining determinant families admit explicit positive-coefficient
certificates recorded in the v2 manuscript and symbolic audit script.

## Independent reconstruction route

The v2 verifier does **not** start from the closed (q_{s,k}) formulas.
It starts from the published AHR (r=6) product identity,

[
E_6(x,y)=
\frac{(1+xy)(1+x^3y)^3(1+x^5y)}
{(1-x^2y)^3(1-x^4y)^2},
]

extracts ([y^s]E_6) exactly over the integers, divides exactly by (1+x),
and compares the resulting (P_s) to the closed formula.

## Truth boundary

- The all-(s) result is established by symbolic algebra in the manuscript,
  not by a finite scan.
- The software provides independent reconstruction, regression tests, and
  tamper-evident receipts.
- Historical priority for the (s=7) threshold remains subject to a complete
  specialist literature review.
- The work is not peer reviewed or journal accepted at this stage.
