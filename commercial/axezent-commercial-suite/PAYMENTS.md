# AXEZENT Payments

## Payment destination

**Cash App Cashtag: $axezent**

## Access rule

Payment and software access are intentionally separate steps:

1. Customer pays the required amount to **$axezent**.
2. The payment is verified by the AXEZENT payment/entitlement backend or an authorized manual verification process.
3. A verified payment creates or extends the customer's entitlement.
4. The customer application checks that entitlement before premium operations.
5. When the entitlement expires or is revoked, premium operations stop until access is renewed.

## Security rule

Do not unlock software from:
- screenshots;
- typed claims of payment;
- transaction IDs supplied only by the customer;
- client-side flags;
- editable local files.

The entitlement backend is the authority.

## Customer privacy

The licensing system should not collect customer proofs, unpublished mathematics, source code, research files, prompts, or other research content as payment telemetry.

## Cash App integration status

The public Cashtag is configured as **$axezent**.

Automatic Cash App payment verification is not yet deployed in this repository. Until a verified merchant/API integration is connected, payment confirmation must be recorded through an authorized manual process before an entitlement is issued.

No Cash App password, PIN, account credential, private API secret, or customer financial credential belongs in this repository.
