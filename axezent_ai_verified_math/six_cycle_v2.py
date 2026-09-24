"""Independent AHR reproducer and v2 certificates for the six-cycle family.

This module is deliberately separate from six_cycle.py.  The legacy module starts
from the closed coefficient formulas in the public preprint.  This module instead
starts from the Adin--Hegedus--Roichman r=6 product identity

    E_6(x,y) =
      (1+xy)(1+x^3 y)^3(1+x^5 y)
      / ((1-x^2 y)^3(1-x^4 y)^2),

extracts [y^s]E_6 exactly over the integers, divides exactly by 1+x, and only
then compares the resulting coefficients with the closed formula.

No floating point arithmetic is used.
"""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from math import comb
from typing import Any

from .six_cycle import p_coefficients


SOURCE_ID_V2 = "Snelling_Six_Cycle_Hook_Unimodality_v2_2026-09-24"


def _validate_s(s: int) -> None:
    if isinstance(s, bool) or not isinstance(s, int) or s < 1:
        raise ValueError("s must be an integer >= 1")


def _poly_add(a: dict[int, int], b: dict[int, int]) -> dict[int, int]:
    out = dict(a)
    for exponent, coefficient in b.items():
        out[exponent] = out.get(exponent, 0) + coefficient
        if out[exponent] == 0:
            del out[exponent]
    return out


def _poly_mul(a: dict[int, int], b: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            exponent = ea + eb
            out[exponent] = out.get(exponent, 0) + ca * cb
    return {e: c for e, c in out.items() if c}


def _y_poly_mul(
    a: dict[int, dict[int, int]],
    b: dict[int, dict[int, int]],
    max_y: int,
) -> dict[int, dict[int, int]]:
    out: dict[int, dict[int, int]] = {}
    for ya, pa in a.items():
        for yb, pb in b.items():
            degree = ya + yb
            if degree <= max_y:
                out[degree] = _poly_add(
                    out.get(degree, {}),
                    _poly_mul(pa, pb),
                )
    return out


def _numerator_y_coefficients(max_y: int) -> dict[int, dict[int, int]]:
    one_plus_xy = {0: {0: 1}, 1: {1: 1}}
    one_plus_x3y_cubed = {
        j: {3 * j: comb(3, j)}
        for j in range(4)
    }
    one_plus_x5y = {0: {0: 1}, 1: {5: 1}}
    return _y_poly_mul(
        _y_poly_mul(one_plus_xy, one_plus_x3y_cubed, max_y),
        one_plus_x5y,
        max_y,
    )


def _denominator_y_coefficient(n: int) -> dict[int, int]:
    """Return [y^n](1-x^2 y)^-3 (1-x^4 y)^-2 exactly."""
    out: dict[int, int] = {}
    for a in range(n + 1):
        b = n - a
        coefficient = comb(a + 2, 2) * (b + 1)
        exponent = 2 * a + 4 * b
        out = _poly_add(out, {exponent: coefficient})
    return out


def one_plus_x_m_from_ahr(s: int) -> list[int]:
    """Return coefficients of (1+x)M_(6^s) from the AHR product."""
    _validate_s(s)
    numerator = _numerator_y_coefficients(s)
    out: dict[int, int] = {}
    for j, x_poly in numerator.items():
        if j <= s:
            out = _poly_add(
                out,
                _poly_mul(x_poly, _denominator_y_coefficient(s - j)),
            )
    max_exponent = max(out)
    return [out.get(i, 0) for i in range(max_exponent + 1)]


def _divide_by_one_plus_x_exact(coefficients: list[int]) -> list[int]:
    if len(coefficients) < 2:
        raise ArithmeticError("expected a nonconstant polynomial")
    quotient = [0] * (len(coefficients) - 1)
    quotient[0] = coefficients[0]
    for i in range(1, len(quotient)):
        quotient[i] = coefficients[i] - quotient[i - 1]
    if coefficients[-1] != quotient[-1]:
        raise ArithmeticError("AHR coefficient is not exactly divisible by 1+x")
    return quotient


def p_coefficients_from_ahr(s: int) -> list[int]:
    """Independently derive P_s from the AHR generating function."""
    _validate_s(s)
    m_coefficients = _divide_by_one_plus_x_exact(one_plus_x_m_from_ahr(s))
    shift = 2 * s - 1
    if any(m_coefficients[:shift]):
        raise ArithmeticError("unexpected coefficient below x^(2s-1)")
    out = m_coefficients[shift:]
    while out and out[-1] == 0:
        out.pop()
    if len(out) != 2 * s + 2:
        raise ArithmeticError("unexpected P_s coefficient count")
    return out


def raw_log_concavity_determinants(s: int) -> list[int]:
    """Return q_k^2-q_(k-1)q_(k+1) for all internal positions."""
    coefficients = p_coefficients(s)
    return [
        coefficients[k] * coefficients[k]
        - coefficients[k - 1] * coefficients[k + 1]
        for k in range(1, len(coefficients) - 1)
    ]


def is_raw_strictly_log_concave(s: int) -> bool:
    _validate_s(s)
    return all(value > 0 for value in raw_log_concavity_determinants(s))


def threshold_statement_holds(s: int) -> bool:
    """Finite-instance audit of the theorem: raw strict LC iff s>=7."""
    _validate_s(s)
    return is_raw_strictly_log_concave(s) == (s >= 7)


def _canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def certificate_v2(s: int) -> dict[str, Any]:
    """Create a v2 receipt binding AHR reconstruction to the threshold checks."""
    _validate_s(s)
    ahr = p_coefficients_from_ahr(s)
    closed = p_coefficients(s)
    determinants = raw_log_concavity_determinants(s)
    payload: dict[str, Any] = {
        "schema": "axezent.six_cycle.certificate.v2",
        "source": SOURCE_ID_V2,
        "family": "(6^s)",
        "s": s,
        "checks": {
            "ahr_reconstruction_matches_closed_formula": ahr == closed,
            "raw_strict_log_concavity": all(value > 0 for value in determinants),
            "raw_strict_log_concavity_expected": s >= 7,
            "phase_transition_instance_matches": threshold_statement_holds(s),
        },
        "p_coefficients": closed,
        "raw_log_concavity_determinants": determinants,
        "scope": (
            "Exact finite-instance receipt.  The all-s threshold theorem is proved "
            "symbolically in the v2 manuscript; this receipt does not replace that proof."
        ),
    }
    payload["sha256"] = hashlib.sha256(
        _canonical_json(payload).encode("utf-8")
    ).hexdigest()
    return payload


def verify_certificate_v2(receipt: dict[str, Any]) -> bool:
    if not isinstance(receipt, dict) or "sha256" not in receipt or "s" not in receipt:
        return False
    supplied = deepcopy(receipt)
    digest = supplied.pop("sha256", None)
    expected_digest = hashlib.sha256(
        _canonical_json(supplied).encode("utf-8")
    ).hexdigest()
    if digest != expected_digest:
        return False
    try:
        expected = certificate_v2(int(receipt["s"]))
    except (TypeError, ValueError, ArithmeticError):
        return False
    return receipt == expected
