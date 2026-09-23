"""AXEZENT license administration CLI.

Use only after an authorized payment/contract check. The signing secret is read
from AXZ_LICENSE_SECRET and is never printed.
"""

from __future__ import annotations

import argparse
import os
import time

from .entitlements import issue_license


def main() -> None:
    parser = argparse.ArgumentParser(prog="axezent-license-issue")
    parser.add_argument("--product", required=True, help="AXEZENT product ID")
    parser.add_argument("--customer", required=True, help="internal customer/account ID")
    parser.add_argument("--days", required=True, type=int, help="entitlement lifetime in days")
    parser.add_argument("--feature", action="append", default=[], help="feature ID; repeat as needed")
    parser.add_argument("--installation", help="optional installation binding")
    args = parser.parse_args()

    if args.days < 1:
        raise SystemExit("--days must be >= 1")

    secret = os.environ.get("AXZ_LICENSE_SECRET")
    if not secret:
        raise SystemExit("AXZ_LICENSE_SECRET is required and must remain private")

    expires = int(time.time()) + args.days * 86400
    token = issue_license(
        secret,
        product_id=args.product,
        customer_id=args.customer,
        expires_at=expires,
        features=args.feature,
        installation_id=args.installation,
    )
    print(token)


if __name__ == "__main__":
    main()
