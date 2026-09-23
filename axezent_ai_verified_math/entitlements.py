"""AXEZENT signed entitlement tokens.

Public implementation, private secret. The signing secret must never be committed
to source control. Tokens are HMAC-SHA256 signed and time-limited.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
from typing import Any


TOKEN_VERSION = "v1"


def _b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")


def _b64url_decode(text: str) -> bytes:
    padding = "=" * (-len(text) % 4)
    return base64.urlsafe_b64decode(text + padding)


def _canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _validate_secret(secret: str | bytes) -> bytes:
    raw = secret.encode("utf-8") if isinstance(secret, str) else secret
    if not isinstance(raw, (bytes, bytearray)) or len(raw) < 32:
        raise ValueError("AXEZENT license signing secret must be at least 32 bytes")
    return bytes(raw)


def issue_license(
    secret: str | bytes,
    *,
    product_id: str,
    customer_id: str,
    expires_at: int,
    features: list[str] | None = None,
    installation_id: str | None = None,
) -> str:
    """Issue a signed, time-limited entitlement token after payment is verified."""
    key = _validate_secret(secret)
    if not product_id or not customer_id:
        raise ValueError("product_id and customer_id are required")
    if not isinstance(expires_at, int) or expires_at <= 0:
        raise ValueError("expires_at must be a positive Unix timestamp")

    payload = {
        "version": TOKEN_VERSION,
        "productId": product_id,
        "customerId": customer_id,
        "expiresAt": expires_at,
        "features": sorted(set(features or [])),
    }
    if installation_id:
        payload["installationId"] = installation_id

    encoded = _b64url_encode(_canonical_json(payload))
    signing_input = f"{TOKEN_VERSION}.{encoded}".encode("ascii")
    signature = hmac.new(key, signing_input, hashlib.sha256).digest()
    return f"{TOKEN_VERSION}.{encoded}.{_b64url_encode(signature)}"


def verify_license(
    secret: str | bytes,
    token: str,
    *,
    product_id: str,
    installation_id: str | None = None,
    now: int,
) -> dict[str, Any]:
    """Verify signature, product scope, installation binding, and expiration."""
    key = _validate_secret(secret)
    result: dict[str, Any] = {
        "allowed": False,
        "productId": product_id,
        "features": [],
    }

    try:
        version, encoded, sig_text = token.split(".", 2)
        if version != TOKEN_VERSION:
            result["reason"] = "unsupported_token_version"
            return result

        signing_input = f"{version}.{encoded}".encode("ascii")
        expected = hmac.new(key, signing_input, hashlib.sha256).digest()
        supplied = _b64url_decode(sig_text)
        if not hmac.compare_digest(expected, supplied):
            result["reason"] = "invalid_signature"
            return result

        payload = json.loads(_b64url_decode(encoded).decode("utf-8"))
    except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
        result["reason"] = "malformed_token"
        return result

    if payload.get("productId") != product_id:
        result["reason"] = "product_mismatch"
        return result

    bound_installation = payload.get("installationId")
    if bound_installation and bound_installation != installation_id:
        result["reason"] = "installation_mismatch"
        return result

    expires_at = payload.get("expiresAt")
    if not isinstance(expires_at, int) or now >= expires_at:
        result["reason"] = "expired"
        return result

    features = payload.get("features", [])
    if not isinstance(features, list) or not all(isinstance(x, str) for x in features):
        result["reason"] = "invalid_features"
        return result

    result.update(
        {
            "allowed": True,
            "expiresAt": expires_at,
            "features": features,
            "customerId": payload.get("customerId"),
        }
    )
    return result
