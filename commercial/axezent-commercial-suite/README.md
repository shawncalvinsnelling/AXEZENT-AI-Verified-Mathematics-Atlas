# AXEZENT Commercial Software Suite

Public commercial product shells for 26 AXEZENT mathematical research and verification ventures.

## Payment

Primary customer-facing payment destination:

**Cash App: $axezent**

See [PAYMENTS.md](./PAYMENTS.md) for the activation rules.

A Cash App payment, payment note, or screenshot does **not** by itself unlock premium software. Premium access is granted only after the AXEZENT entitlement service records the payment as verified.

## Subscription architecture

```
customer -> Cash App $axezent
             |
             v
       payment verified
             |
             v
public GitHub client
        |
        v
phone-home entitlement check
        |
        +-- active entitlement --> paid API / private computation
        |
        +-- expired / unpaid --> premium operation denied
```

The private discovery/search/scoring engine is **not included** in this repository.

A local license check in public source code can be removed, so valuable paid computation must remain behind a private service that independently verifies entitlement. Expired or unpaid subscriptions simply stop premium operations. There is no self-deletion, destructive behavior, hidden persistence, or anti-analysis mechanism.

See:
- [VENTURES.md](./VENTURES.md)
- [products.json](./products.json)
- [PAYMENTS.md](./PAYMENTS.md)
- [PRICING.md](./PRICING.md)
- [ENTERPRISE.md](./ENTERPRISE.md)
- [IP_GOVERNANCE.md](./IP_GOVERNANCE.md)
- [CORPORATE_STANDARD.md](./CORPORATE_STANDARD.md)
- [licensing/](./licensing/)
- [COMMERCIAL_TERMS.md](./COMMERCIAL_TERMS.md)
- [PRIVACY_BOUNDARY.md](./PRIVACY_BOUNDARY.md)

## Legal entity boundary

These are software brands/product ventures, not incorporated legal entities. LLC/corporation formation, banking, tax registration, trademarks, contracts, and insurance are separate business steps.
