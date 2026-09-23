# Production entitlement backend

The production backend should remain private.

Recommended flow:

1. Customer purchases/subscribes through the billing provider.
2. A verified billing webhook updates the private entitlement database.
3. The public client calls `/v1/entitlements/check`.
4. The server checks account status, product, installation/device policy, expiration, revocation, and feature tier.
5. Paid APIs independently re-check authorization server-side.
6. If payment expires, premium API calls are denied. No destructive action is taken on customer devices.

Do not rely on public client-side code alone for enforcement.

Never commit billing API secrets, webhook signing secrets, entitlement database credentials, private signing keys, or customer license keys.
