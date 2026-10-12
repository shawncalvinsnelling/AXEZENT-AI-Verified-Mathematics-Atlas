#!/usr/bin/env python3
"""Exact-interval, finite-domain certificate for a Chebyshev error envelope.

No RH assumption is used. No claim is made beyond the stated finite interval.
Natural logarithms and square roots are bounded using integer arithmetic.
All checks remain active under python -O. Python 3.11+; standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

BITS = 96
SCALE = 1 << BITS
TERMS = 40


def ceildiv(a: int, b: int) -> int:
    if a < 0 or b <= 0:
        raise ValueError('ceildiv expects a >= 0 and b > 0')
    return (a + b - 1) // b


def log_ratio_interval(num: int, den: int) -> tuple[int, int]:
    """Enclose SCALE*log(num/den) when 1 <= num/den <= 2.

    z=(num-den)/(num+den) in [0,1/3]. Use
      log(num/den) = 2 sum_{j>=0} z^(2j+1)/(2j+1).
    Rounded interval products enclose every term. The positive remainder is
    <= 2*3^(-2*TERMS-1)/((2*TERMS+1)*(1-1/9)).
    """
    if den < 1 or not den <= num <= 2 * den:
        raise ValueError('requires positive integers and 1 <= ratio <= 2')
    if num == den:
        return 0, 0
    a, b = num - den, num + den
    zlo, zhi = (a * SCALE) // b, ceildiv(a * SCALE, b)
    z2lo = zlo * zlo // SCALE
    z2hi = ceildiv(zhi * zhi, SCALE)
    plo, phi = zlo, zhi
    slo = shi = 0
    for j in range(TERMS):
        odd = 2 * j + 1
        slo += plo // odd
        shi += ceildiv(phi, odd)
        plo = plo * z2lo // SCALE
        phi = ceildiv(phi * z2hi, SCALE)
    tail = ceildiv(9 * SCALE, 4 * (2 * TERMS + 1) * 3 ** (2 * TERMS + 1))
    return 2 * slo, 2 * shi + tail


LN2_LO, LN2_HI = log_ratio_interval(2, 1)


def log_integer_interval(n: int) -> tuple[int, int]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError('n must be a positive integer')
    k = n.bit_length() - 1
    lo, hi = log_ratio_interval(n, 1 << k)
    return k * LN2_LO + lo, k * LN2_HI + hi


def sieve_primes(limit: int) -> list[int]:
    flags = bytearray(b'\x01') * (limit + 1)
    flags[0:2] = b'\x00\x00'
    for p in range(2, math.isqrt(limit) + 1):
        if flags[p]:
            count = (limit - p * p) // p + 1
            flags[p * p:limit + 1:p] = b'\x00' * count
    return [n for n in range(2, limit + 1) if flags[n]]


def prime_power_events(limit: int) -> list[tuple[int, int]]:
    events: list[tuple[int, int]] = []
    for p in sieve_primes(limit):
        q = p
        while q <= limit:
            events.append((q, p))
            q *= p
    events.sort()
    if len({q for q, _ in events}) != len(events):
        raise ArithmeticError('duplicate prime-power event')
    return events


def check_cell(a: int, b: int, psi_lo: int, psi_hi: int,
               constant_denominator: int) -> tuple[int, int]:
    """For a <= x < b with constant psi, certify all-real error at once.

    |psi-x| is bounded by its four interval-corner values.
    sqrt(x)*log(x)^2 is increasing on x>=1, so its rigorous lower
    bound at a is a valid lower bound on the entire cell.
    """
    if not 2 <= a <= b or psi_lo > psi_hi or constant_denominator <= 0:
        raise ValueError('invalid interval or bound')
    error_upper = max(abs(p - x * SCALE)
                      for p in (psi_lo, psi_hi) for x in (a, b))
    lnlo, _ = log_integer_interval(a)
    sqrtlo = math.isqrt(a * SCALE * SCALE)
    bound_lower = sqrtlo * lnlo * lnlo // (constant_denominator * SCALE * SCALE)
    if error_upper > bound_lower:
        raise ArithmeticError(f'no certificate on [{a},{b}]: '
                              f'error_upper_scaled={error_upper}, '
                              f'bound_lower_scaled={bound_lower}')
    return error_upper, bound_lower


def certify(start: int = 256, stop: int = 1 << 20,
            constant_denominator: int = 16) -> dict:
    if start < 2 or stop <= start:
        raise ValueError('require 2 <= start < stop')
    events = prime_power_events(stop)
    cache: dict[int, tuple[int, int]] = {}
    psi_lo = psi_hi = 0
    cells = 0
    digest = hashlib.sha256()
    worst: tuple[int, int, int, int] = (0, 1, start, start)
    min_margin: int | None = None
    shelves: dict[str, int] = {}
    a = start
    for q, p in events:
        if q > start:
            e, bound = check_cell(a, q, psi_lo, psi_hi, constant_denominator)
            cells += 1
            key = str(a.bit_length() - 1)
            shelves[key] = shelves.get(key, 0) + 1
            digest.update(json.dumps([a, q, psi_lo, psi_hi, e, bound],
                                     separators=(',', ':')).encode() + b'\n')
            if e * worst[1] > worst[0] * bound:
                worst = (e, bound, a, q)
            margin = bound - e
            min_margin = margin if min_margin is None else min(min_margin, margin)
            a = q
        if p not in cache:
            cache[p] = log_integer_interval(p)
        lo, hi = cache[p]
        psi_lo += lo
        psi_hi += hi
    # In case stop is not a prime power, finish the final constant cell.
    if a < stop:
        e, bound = check_cell(a, stop, psi_lo, psi_hi, constant_denominator)
        cells += 1
        key = str(a.bit_length() - 1)
        shelves[key] = shelves.get(key, 0) + 1
        digest.update(json.dumps([a, stop, psi_lo, psi_hi, e, bound],
                                 separators=(',', ':')).encode() + b'\n')
        if e * worst[1] > worst[0] * bound:
            worst = (e, bound, a, stop)
        margin = bound - e
        min_margin = margin if min_margin is None else min(min_margin, margin)
    # Endpoint psi(stop), including any jump at stop, is separately checked.
    end_e, end_bound = check_cell(stop, stop, psi_lo, psi_hi, constant_denominator)
    digest.update(json.dumps(['right_endpoint', stop, psi_lo, psi_hi, end_e, end_bound],
                             separators=(',', ':')).encode() + b'\n')
    return {
        'status': 'PASS_EXACT_INTERVAL_FINITE_DOMAIN',
        'statement': f'For every real x in [{start}, {stop}], '
                     f'abs(psi(x)-x) <= sqrt(x)*log(x)^2/{constant_denominator}',
        'x_min': start, 'x_max': stop, 'constant': f'1/{constant_denominator}',
        'scope': 'FINITE_DOMAIN_ALL_REAL_X_NOT_RH',
        'prime_count_up_to_stop': len(cache),
        'prime_power_events_up_to_stop': len(events),
        'constant_psi_cells_certified': cells,
        'right_endpoint_checked': True,
        'dyadic_cells_by_floor_log2_left_endpoint': shelves,
        'rigorous_log_scale': str(SCALE), 'log_series_terms': TERMS,
        'worst_conservative_cell': {
            'left': worst[2], 'right': worst[3],
            'ratio_numerator': str(worst[0]), 'ratio_denominator': str(worst[1]),
            'ratio_approx_for_display_only': worst[0] / worst[1]
        },
        'minimum_cell_margin_scaled': str(min_margin),
        'right_endpoint_margin_scaled': str(end_bound - end_e),
        'ordered_exact_cell_sha256': digest.hexdigest(),
        'arithmetic': 'Integer intervals; no floats used to accept any inequality',
        'unproved_extension': 'No certificate or theorem covers x beyond x_max',
        'novelty': 'Not claimed', 'formal_kernel_verified': False,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--start', type=int, default=256)
    ap.add_argument('--stop', type=int, default=1 << 20)
    ap.add_argument('--output', type=Path, default=Path('finite_envelope_receipt.json'))
    args = ap.parse_args()
    result = certify(args.start, args.stop)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
