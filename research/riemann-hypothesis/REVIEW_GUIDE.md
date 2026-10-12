# Reviewer guide

Thank you for reviewing this work. Review the exact statement rather than the AXEZENT name, a badge, a passing workflow, or an AI-generated endorsement. No outside review has yet been recorded for this edition.

## Two separate review tasks

**Mathematical review:** In `MATHEMATICAL_NOTE.md`, audit the initial partial-summation identity, locally uniform convergence, logarithmic-derivative poles and zero symmetry (Theorem A); the all-real dyadic hypothesis and geometric factor (B); the scope of the absolute-value obstruction (C); and the complete cell coverage with jump conventions (D). The unproved hypothesis in A/B is not hidden in the finite certificate.

**Computational review:** Read the small standalone verifier. Run `python replay.py`. Check outward rounding, the log-series remainder, integer square-root enclosure, prime-power enumeration, endpoint treatment and failure behavior. An independently written verifier is particularly valuable. Distinguish rerunning the same program from independent implementation.

## Report a mathematical objection

Open an issue titled `[RH review] <short objection>` or comment on the publication pull request. Supply:

- The exact commit and claim ID.
- File, section, equation or code line.
- The proposed gap, missing assumption or counterexample with its domain.
- A detailed argument or minimal reproduction.
- Whether the concern affects a conditional implication, the finite certificate, or the unproved global hypothesis.

## Report reproduction

Use `[RH reproduction] <platform / result>`, giving commit, Python version, operating system, commands, exit status, full output or log attachment, receipt comparison, and any modifications. Do not include credentials or personal data. A reproduction report need not assert the mathematical note is correct in its entirety.

## Contribution and correction policy

Discuss a concrete mathematical or code issue before proposing a change. Preserve failed examples and identify the exact effect on claim status. Keep code review, internal mathematical checking, external specialist review, formal-kernel verification and publication/priority judgments separate. A merge is not a mathematical endorsement. No badge-oriented or trivial duplicate pull requests are requested.

The existing Atlas license remains in effect; no new general redistribution or modification license is conferred by this guide. The supplied scripts are public research-evaluation tools under that notice.

## Highest-priority open question

Can one derive an unconditional all-scale bound for the actual signed quantity

$$D(x)=\psi(2x)-\psi(x)-x$$

with fixed K and X0, $|D(x)|\le K\sqrt{x}(\log x)^2$ for every real x >= X0, or an alternative sufficient bound on G? This is an RH-strength question, not a small numerical task being advertised as solved. Finite checks do not settle it.

## Public-review status

This package is being offered for open technical scrutiny. Hosting it on GitHub is not journal peer review and does not mean a specialist has accepted it. We welcome precise corrections as well as confirmed reproductions.
