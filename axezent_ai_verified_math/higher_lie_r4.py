"""Exact checker for the all-s r=4 higher-Lie hook-multiplicity formula.

The mathematical proof is in docs/HIGHER_LIE_R4_ALL_S.md.  This module is a
finite exact regression checker for the coefficient extraction used there.
It is not the reason the universal theorem is true.
"""


def e4_coefficients(s: int) -> dict[int, int]:
    """Return [y^s] E_4(x,y) as an exact sparse polynomial in x."""
    if s < 0:
        raise ValueError("s must be nonnegative")

    # (1 + x y)(1 + x^3 y) = 1 + (x+x^3)y + x^4 y^2
    numerator = ((0, 0, 1), (1, 1, 1), (3, 1, 1), (4, 2, 1))
    out: dict[int, int] = {}
    for xdeg, ydeg, coeff in numerator:
        t = s - ydeg
        if t < 0:
            continue
        # [y^t](1-x^2 y)^(-2) = (t+1)x^(2t)
        deg = xdeg + 2 * t
        out[deg] = out.get(deg, 0) + coeff * (t + 1)
    return {k: v for k, v in sorted(out.items()) if v}


def expected_e4_coefficients(s: int) -> dict[int, int]:
    if s == 0:
        return {0: 1}
    return {
        2 * s - 1: s,
        2 * s: 2 * s,
        2 * s + 1: s,
    }


def hook_multiplicities_from_e(s: int) -> list[int]:
    """Invert e_k=m_k+m_(k-1), with m_-1=m_(4s)=0."""
    if s < 1:
        raise ValueError("s must be positive")
    n = 4 * s
    e = e4_coefficients(s)
    m: list[int] = []
    prev = 0
    for k in range(n):
        cur = e.get(k, 0) - prev
        m.append(cur)
        prev = cur
    assert e.get(n, 0) == prev
    return m


def expected_hook_multiplicities(s: int) -> list[int]:
    if s < 1:
        raise ValueError("s must be positive")
    m = [0] * (4 * s)
    m[2 * s - 1] = s
    m[2 * s] = s
    return m


def is_unimodal(a: list[int]) -> bool:
    if not a:
        return True
    peak = max(range(len(a)), key=a.__getitem__)
    return all(a[i] <= a[i + 1] for i in range(peak)) and all(
        a[i] >= a[i + 1] for i in range(peak, len(a) - 1)
    )


def is_log_concave(a: list[int]) -> bool:
    return all(a[i] * a[i] >= a[i - 1] * a[i + 1]
               for i in range(1, len(a) - 1))


def audit(limit: int = 10000) -> dict[str, int | str]:
    for s in range(1, limit + 1):
        assert e4_coefficients(s) == expected_e4_coefficients(s)
        m = hook_multiplicities_from_e(s)
        assert m == expected_hook_multiplicities(s)
        assert is_unimodal(m)
        assert is_log_concave(m)
    return {
        "status": "PASS",
        "family": "(4^s)",
        "s_min": 1,
        "s_max": limit,
        "exact_cases": limit,
    }


if __name__ == "__main__":
    print(audit())
