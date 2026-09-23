# AXEZENT Entitlement Service

AXEZENT premium access uses signed, time-limited entitlements.

## Payment-to-access flow

1. Customer pays through an approved AXEZENT payment channel.
2. AXEZENT independently verifies the payment or contract.
3. An authorized operator issues a signed entitlement token.
4. The customer client phones home to `/v1/entitlements/check`.
5. The server verifies signature, product scope, installation binding (when used), and expiration.
6. Active access permits the paid operation; expired access does not.

## Signing secret

The signing secret must be at least 32 bytes and must stay outside GitHub and customer software.

Set it only in the authorized server/admin environment as `AXZ_LICENSE_SECRET`.

## Current Cash App flow

Cash App **$axezent** is the public payment destination. Automatic Cash App merchant/API verification remains a separate integration. Until that connection is deployed, AXEZENT must verify payment before issuing an entitlement.

## Reference service

The repository includes `reference_server.py` as an implementation of the public API contract. Internet production use should add HTTPS termination, rate limiting, monitoring, backups, and normal production hardening.
