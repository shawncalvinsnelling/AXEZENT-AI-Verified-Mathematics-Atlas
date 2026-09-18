from axezent_ai_verified_math.higher_lie_r4 import (
    audit,
    e4_coefficients,
    expected_e4_coefficients,
    expected_hook_multiplicities,
    hook_multiplicities_from_e,
    is_log_concave,
    is_unimodal,
)


def test_small_exact_rows():
    for s in range(1, 101):
        assert e4_coefficients(s) == expected_e4_coefficients(s)
        m = hook_multiplicities_from_e(s)
        assert m == expected_hook_multiplicities(s)
        assert is_unimodal(m)
        assert is_log_concave(m)


def test_beyond_published_rectangular_check_range():
    # The cited 2023 paper reports rectangular checks only through s <= 5.
    for s in (6, 7, 10, 25, 100, 1000):
        assert hook_multiplicities_from_e(s) == expected_hook_multiplicities(s)


def test_large_exact_regression():
    receipt = audit(10000)
    assert receipt["status"] == "PASS"
    assert receipt["exact_cases"] == 10000
