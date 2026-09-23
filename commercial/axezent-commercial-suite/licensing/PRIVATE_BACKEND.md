# Production Entitlement Backend

This document describes a **future production architecture**. It is not a representation that a production backend or recurring-billing integration is currently deployed.

The production backend should remain private.

## Recommended activated-service flow

1. AXEZENT confirms a written order, payment terms, applicable tax handling, and customer acceptance of the governing terms.
2. The customer pays through an approved business payment channel.
3. AXEZENT verifies payment or contract status.
4. A private entitlement database records the customer's authorized product, access period, and feature scope.
5. The public client calls `/v1/entitlements/check`.
6. The server checks account status, product, installation or device policy when used, expiration, revocation, and feature tier.
7. Paid APIs independently re-check authorization server-side.
8. When access expires or is revoked, premium API calls are denied. No destructive action is taken on customer devices.

If automatic recurring billing is introduced later, it should be implemented only after the recurring terms are clearly disclosed and the customer provides express consent.

Do not rely on public client-side code alone for enforcement.

Never commit billing API secrets, webhook signing secrets, entitlement database credentials, private signing keys, customer license keys, or customer financial credentials.

See [Terms of Service](../TERMS_OF_SERVICE.md), [Billing & Activation](../PAYMENTS.md), and [Privacy Policy](../PRIVACY_POLICY.md).
