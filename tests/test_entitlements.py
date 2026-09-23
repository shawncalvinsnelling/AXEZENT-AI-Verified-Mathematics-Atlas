from axezent_ai_verified_math.entitlements import issue_license, verify_license

SECRET = "S" * 32

def token(**kw):
    params = dict(
        product_id="six-cycle-certifier",
        customer_id="cust-001",
        expires_at=2000,
        features=["premium-analysis", "certificate-export"],
        installation_id="install-abc",
    )
    params.update(kw)
    return issue_license(SECRET, **params)

def test_valid_entitlement():
    result = verify_license(
        SECRET, token(),
        product_id="six-cycle-certifier",
        installation_id="install-abc",
        now=1000,
    )
    assert result["allowed"] is True
    assert result["expiresAt"] == 2000
    assert result["features"] == ["certificate-export", "premium-analysis"]

def test_expired_entitlement():
    result = verify_license(
        SECRET, token(),
        product_id="six-cycle-certifier",
        installation_id="install-abc",
        now=2000,
    )
    assert result["allowed"] is False
    assert result["reason"] == "expired"

def test_product_mismatch():
    result = verify_license(
        SECRET, token(),
        product_id="proof-qa-system",
        installation_id="install-abc",
        now=1000,
    )
    assert result["allowed"] is False
    assert result["reason"] == "product_mismatch"

def test_installation_mismatch():
    result = verify_license(
        SECRET, token(),
        product_id="six-cycle-certifier",
        installation_id="other",
        now=1000,
    )
    assert result["allowed"] is False
    assert result["reason"] == "installation_mismatch"

def test_tamper_detection():
    original = token()
    version, payload, signature = original.split(".")
    replacement = ("A" if payload[0] != "A" else "B") + payload[1:]
    result = verify_license(
        SECRET, ".".join([version, replacement, signature]),
        product_id="six-cycle-certifier",
        installation_id="install-abc",
        now=1000,
    )
    assert result["allowed"] is False
