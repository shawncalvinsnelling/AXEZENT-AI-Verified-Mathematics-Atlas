# AXEZENT Entitlement Service

AXEZENT premium access is designed around signed, time-limited entitlements.

## Payment-to-access flow

For an activated paid service:

1. AXEZENT confirms a written order, product scope, price, access period, applicable tax handling, and approved payment channel.
2. The customer affirmatively accepts the order and governing terms.
3. The customer pays through the approved channel.
4. AXEZENT independently verifies the payment or contract.
5. An authorized operator issues a signed entitlement token.
6. The customer client calls `/v1/entitlements/check`.
7. The service verifies signature, product scope, installation binding when used, expiration, and revocation.
8. Active access permits the paid operation; expired access does not.

## Signing secret

The signing secret must be at least 32 bytes and must stay outside GitHub and customer software.

Set it only in the authorized server/admin environment as `AXZ_LICENSE_SECRET`.

## Payment-provider boundary

Do not publish a payment destination as an unconditional invitation to send money.

If Cash App is used for a goods-or-services transaction, use it only through an account configuration permitted for business sales and provide the current payment instructions for the specific order.

Automatic merchant/API verification remains a separate integration. Until a production integration is deployed, payment confirmation and entitlement issuance are manual.

## Reference service

The repository includes `reference_server.py` as a reference implementation of the public API contract. It is not a representation that the production entitlement backend is deployed.

Internet production use should add HTTPS termination, rate limiting, monitoring, backups, access controls, secret management, and ordinary production hardening.

See [Billing & Activation](../PAYMENTS.md), [Terms of Service](../TERMS_OF_SERVICE.md), and the [Privacy Policy](../PRIVACY_POLICY.md).
