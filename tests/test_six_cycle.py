from copy import deepcopy

import pytest

from axezent_ai_verified_math.six_cycle import (
    certificate,
    is_strictly_log_concave_on_support,
    is_unimodal,
    multiply_by_one_plus_x,
    p_coefficients,
    verify_certificate,
)


def test_known_coefficients():
    assert p_coefficients(1) == [1, 2, 1, 1]
    assert p_coefficients(2) == [3, 6, 5, 5, 4, 2]
    assert p_coefficients(3) == [6, 13, 14, 16, 15, 11, 7, 3]


@pytest.mark.parametrize("s", range(1, 251))
def test_published_family_regression(s):
    p = p_coefficients(s)
    b = multiply_by_one_plus_x(p)
    assert len(p) == 2 * s + 2
    assert all(x > 0 for x in p)
    assert is_unimodal(p)
    assert is_strictly_log_concave_on_support(b)


def test_certificate_round_trip_and_tamper_detection():
    receipt = certificate(37)
    assert verify_certificate(receipt)

    tampered = deepcopy(receipt)
    tampered["p_coefficients"][0] += 1
    assert not verify_certificate(tampered)


@pytest.mark.parametrize("bad", [0, -1, 1.5, True, "3"])
def test_invalid_s_rejected(bad):
    with pytest.raises(ValueError):
        p_coefficients(bad)
