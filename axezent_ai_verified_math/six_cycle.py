"""Exact public certifier for the Snelling six-cycle hook-unimodality family.

This module implements the coefficient formulas stated in the public preprint
"Six-Cycle Insertion and Hook-Unimodality in Higher Lie Characters" (2026).

It verifies the published family; it is not the private AXEZENT discovery engine.
"""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from typing import Any


SOURCE_ID = "Snelling_Six_Cycle_Hook_Unimodality_2026-09-22"


def _validate_s(s: int) -> None:
    if isinstance(s, bool) or not isinstance(s, int) or s < 1:
        raise ValueError("s must be an integer >= 1")


def _q_interior(s: int, k: int) -> int:
    num = (
        k**3
        - 4 * k**2 * s
        - 3 * k**2
        + 4 * k * s**2
        + 8 * k * s
        + 6 * k
        - 4 * s**2
        - 6 * s
        - 4
    )
    if num % 2:
        raise ArithmeticError("interior coefficient formula must be integral")
    return num // 2


def p_coefficients(s: int) -> list[int]:
    """Return coefficients q_{s,k} of P_s where M_(6^s)=x^(2s-1) P_s."""
    _validate_s(s)
    coeffs = [
        s * (s + 1) // 2,
        (3 * s**2 - s + 2) // 2,
        (5 * s**2 - 7 * s + 4) // 2,
    ]
    coeffs.extend(_q_interior(s, k) for k in range(3, 2 * s + 1))
    coeffs.append(s)
    if len(coeffs) != 2 * s + 2:
        raise ArithmeticError("unexpected coefficient count")
    return coeffs


def shifted_m_representation(s: int) -> dict[str, Any]:
    """Compact exact representation of M_(6^s)(x)."""
    coeffs = p_coefficients(s)
    return {
        "shift": 2 * s - 1,
        "p_coefficients": coeffs,
        "degree": (2 * s - 1) + (len(coeffs) - 1),
    }


def multiply_by_one_plus_x(coeffs: list[int]) -> list[int]:
    if not coeffs:
        return []
    out = [0] * (len(coeffs) + 1)
    for i, value in enumerate(coeffs):
        out[i] += value
        out[i + 1] += value
    return out


def is_unimodal(coeffs: list[int]) -> bool:
    if not coeffs:
        return True
    peak = max(coeffs)
    first = coeffs.index(peak)
    last = len(coeffs) - 1 - list(reversed(coeffs)).index(peak)
    return (
        all(coeffs[i] <= coeffs[i + 1] for i in range(first))
        and all(value == peak for value in coeffs[first : last + 1])
        and all(coeffs[i] >= coeffs[i + 1] for i in range(last, len(coeffs) - 1))
    )


def is_strictly_log_concave_on_support(coeffs: list[int]) -> bool:
    support = [x for x in coeffs if x != 0]
    if len(support) < 3:
        return True
    if any(x <= 0 for x in support):
        return False
    return all(
        support[i] * support[i] > support[i - 1] * support[i + 1]
        for i in range(1, len(support) - 1)
    )


def _canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def certificate(s: int) -> dict[str, Any]:
    """Create a reproducible exact verification receipt for a chosen s."""
    _validate_s(s)
    p = p_coefficients(s)
    b = multiply_by_one_plus_x(p)
    payload: dict[str, Any] = {
        "schema": "axezent.six_cycle.certificate.v1",
        "source": SOURCE_ID,
        "family": "(6^s)",
        "s": s,
        "m_shift": 2 * s - 1,
        "p_coefficients": p,
        "one_plus_x_p_coefficients": b,
        "checks": {
            "positive_support": all(x > 0 for x in p),
            "unimodal": is_unimodal(p),
            "strict_log_concavity_after_one_plus_x": is_strictly_log_concave_on_support(b),
        },
        "scope": (
            "Exact certificate for the published all-s six-cycle family only; "
            "not a certificate for the full arbitrary-partition conjecture."
        ),
    }
    payload["sha256"] = hashlib.sha256(_canonical_json(payload).encode("utf-8")).hexdigest()
    return payload


def verify_certificate(receipt: dict[str, Any]) -> bool:
    """Verify hash integrity and recompute the exact certificate from s."""
    if not isinstance(receipt, dict) or "sha256" not in receipt or "s" not in receipt:
        return False
    supplied = deepcopy(receipt)
    digest = supplied.pop("sha256", None)
    expected_digest = hashlib.sha256(_canonical_json(supplied).encode("utf-8")).hexdigest()
    if digest != expected_digest:
        return False
    try:
        expected = certificate(int(receipt["s"]))
    except (TypeError, ValueError, ArithmeticError):
        return False
    return receipt == expected
