from copy import deepcopy

import pytest

from axezent_ai_verified_math.six_cycle import p_coefficients
from axezent_ai_verified_math.six_cycle_v2 import (
    certificate_v2,
    is_raw_strictly_log_concave,
    p_coefficients_from_ahr,
    raw_log_concavity_determinants,
    threshold_statement_holds,
    verify_certificate_v2,
)


@pytest.mark.parametrize("s", range(1, 61))
def test_independent_ahr_reconstruction_matches_closed_formula(s):
    assert p_coefficients_from_ahr(s) == p_coefficients(s)


def test_exact_transition_failures_before_seven():
    assert not is_raw_strictly_log_concave(1)
    expected_obstruction = {
        2: -5,
        3: -12,
        4: -21,
        5: -23,
        6: -3,
    }
    for s, value in expected_obstruction.items():
        determinants = raw_log_concavity_determinants(s)
        assert determinants[1] == value
        assert not is_raw_strictly_log_concave(s)


@pytest.mark.parametrize("s", range(7, 251))
def test_raw_strict_log_concavity_from_seven(s):
    assert is_raw_strictly_log_concave(s)
    assert threshold_statement_holds(s)


@pytest.mark.parametrize("s", range(1, 251))
def test_threshold_statement_finite_regression(s):
    assert threshold_statement_holds(s)


def test_v2_certificate_round_trip_and_tamper_detection():
    receipt = certificate_v2(37)
    assert verify_certificate_v2(receipt)

    tampered = deepcopy(receipt)
    tampered["raw_log_concavity_determinants"][0] += 1
    assert not verify_certificate_v2(tampered)


@pytest.mark.parametrize("bad", [0, -1, 1.5, True, "7"])
def test_invalid_s_rejected(bad):
    with pytest.raises(ValueError):
        p_coefficients_from_ahr(bad)
