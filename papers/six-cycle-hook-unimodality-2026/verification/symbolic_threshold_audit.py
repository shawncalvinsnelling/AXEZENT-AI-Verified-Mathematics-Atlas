"""Symbolic identity audit for the exact s=7 log-concavity threshold.

Run with:
    python papers/six-cycle-hook-unimodality-2026/verification/symbolic_threshold_audit.py

This script is an executable cross-check of the algebra printed in the v2
manuscript.  The manuscript proof remains the mathematical proof.
"""

import sympy as sp


s, k = sp.symbols("s k", integer=True, positive=True)
u, a, b = sp.symbols("u a b", integer=True, nonnegative=True)

q0 = s * (s + 1) / 2
q1 = (3 * s**2 - s + 2) / 2
q2 = (5 * s**2 - 7 * s + 4) / 2


def Q(index):
    return (
        index**3
        - 4 * index**2 * s
        - 3 * index**2
        + 4 * index * s**2
        + 8 * index * s
        + 6 * index
        - 4 * s**2
        - 6 * s
        - 4
    ) / 2


delta1 = sp.factor(q1**2 - q0 * q2)
delta2 = sp.factor(q2**2 - q1 * Q(3))
delta3 = sp.factor(Q(3)**2 - q2 * Q(4))
delta_interior = sp.factor(Q(k)**2 - Q(k - 1) * Q(k + 1))
delta_end = sp.factor(Q(2 * s)**2 - Q(2 * s - 1) * s)

assert sp.expand(delta1.subs(s, u + 1)) == (
    u**4 + 3*u**3 + 7*u**2 + 7*u + 3
)
assert sp.expand(delta2.subs(s, u + 7)) == (
    u**4 / 4 + 5*u**3 + sp.Rational(139, 4)*u**2 + 93*u + 60
)
assert sp.expand(delta3.subs(s, u + 2)) == (
    u**4 + sp.Rational(9, 2)*u**3
    + sp.Rational(33, 2)*u**2 + 19*u + 5
)
assert sp.expand(delta_end.subs(s, u + 1)) == 3*u**2 + u + 2

interior_certificate = sp.expand(
    4 * delta_interior.subs({k: a + 4, s: (a + b + 5) / 2})
)
expected_interior = (
    2*a**2*b**2 + 8*a**2*b + 3*a**2
    + 12*a*b**2 + 46*a*b + 14*a
    + b**4 + 8*b**3 + 42*b**2 + 98*b + 47
)
assert sp.expand(interior_certificate - expected_interior) == 0

assert [sp.simplify(delta2.subs(s, n)) for n in range(2, 7)] == [
    -5, -12, -21, -23, -3
]

print("PASS: symbolic s=7 threshold identities verified exactly.")
