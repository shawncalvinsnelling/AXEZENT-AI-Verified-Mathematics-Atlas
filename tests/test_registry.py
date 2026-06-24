from axezent_ai_verified_math.registry import MODULES

def test_required_modules():
    assert len(MODULES) >= 5

def test_no_global_claims():
    assert all("SOLVED" not in str(m).upper() for m in MODULES)
