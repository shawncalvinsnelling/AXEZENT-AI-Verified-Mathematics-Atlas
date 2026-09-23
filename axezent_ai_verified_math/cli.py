"""Command-line interface for public AXEZENT exact certifiers."""

from __future__ import annotations

import argparse
import json

from .six_cycle import certificate


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="axezent-six-cycle",
        description="Generate an exact certificate for the published (6^s) hook-unimodality family.",
    )
    parser.add_argument("s", type=int, help="positive integer s in the partition family (6^s)")
    parser.add_argument("--json", action="store_true", help="emit the complete JSON certificate")
    args = parser.parse_args()

    receipt = certificate(args.s)
    if args.json:
        print(json.dumps(receipt, indent=2, sort_keys=True))
        return

    checks = receipt["checks"]
    print(f"AXEZENT Six-Cycle Certifier — s={receipt['s']}")
    print(f"M_(6^s)(x) = x^{receipt['m_shift']} P_s(x)")
    print("P_s coefficients:", receipt["p_coefficients"])
    print("Unimodal:", checks["unimodal"])
    print(
        "Strict log-concavity of (1+x)P_s:",
        checks["strict_log_concavity_after_one_plus_x"],
    )
    print("Certificate SHA-256:", receipt["sha256"])


if __name__ == "__main__":
    main()
