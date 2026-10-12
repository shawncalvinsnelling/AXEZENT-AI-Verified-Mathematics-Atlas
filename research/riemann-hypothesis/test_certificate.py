from fractions import Fraction
import math
import unittest
from certify_finite_envelope import (
    SCALE, log_integer_interval, log_ratio_interval, sieve_primes,
    prime_power_events, check_cell, certify,
)


def rational_log_interval(n: int, terms: int = 64):
    # Independently formed rational powers, not fixed-point recurrence.
    k = n.bit_length() - 1
    def series(z):
        value = 2 * sum((z ** (2*j+1) / (2*j+1)
                         for j in range(terms)), Fraction())
        tail = 2 * z ** (2*terms+1) / ((2*terms+1)*(1-z*z))
        return value, value + tail
    l2, u2 = series(Fraction(1, 3))
    l, u = series(Fraction(n-(1<<k), n+(1<<k)))
    return k*l2+l, k*u2+u


def eval_poly(coeffs, x):
    y = 0
    for c in reversed(coeffs):
        y = y*x+c
    return y


def exact_identity(p, q, degree, points):
    def deg(c):
        return max((i for i, a in enumerate(c) if a), default=-1)
    if degree < 0 or deg(p) > degree or deg(q) > degree:
        raise ValueError('unjustified degree cap')
    if len(set(points)) < degree + 1:
        raise ValueError('not enough distinct points')
    return all(eval_poly(p, a) == eval_poly(q, a) for a in points)


class ExactCertificateTests(unittest.TestCase):
    def test_log_enclosures_against_fraction_series(self):
        for n in [2,3,6,17,256,343,1000,1048573,1048576]:
            with self.subTest(n=n):
                lo, hi = log_integer_interval(n)
                flo, fhi = rational_log_interval(n)
                self.assertLessEqual(Fraction(lo, SCALE), flo)
                self.assertGreaterEqual(Fraction(hi, SCALE), fhi)
    def test_log_of_one(self):
        self.assertEqual(log_integer_interval(1), (0,0))
    def test_invalid_log_input(self):
        for n in [0,-1,True,2.5]:
            with self.assertRaises(ValueError): log_integer_interval(n)
    def test_invalid_ratio(self):
        with self.assertRaises(ValueError): log_ratio_interval(3,1)
    def test_sieve_vs_trial_division(self):
        expected = [n for n in range(2,5001)
                    if all(n % d for d in range(2,math.isqrt(n)+1))]
        self.assertEqual(sieve_primes(5000), expected)
    def test_prime_power_events_vs_factorization(self):
        actual = dict(prime_power_events(5000))
        expected = {}
        for n in range(2,5001):
            factors = []
            rem = n
            for d in range(2,math.isqrt(n)+1):
                if rem % d == 0:
                    factors.append(d)
                    while rem % d == 0: rem //= d
            if rem > 1: factors.append(rem)
            if len(factors)==1: expected[n]=factors[0]
        self.assertEqual(actual, expected)
    def test_finite_subinterval(self):
        result=certify(256,1024)
        self.assertEqual(result['status'], 'PASS_EXACT_INTERVAL_FINITE_DOMAIN')
        self.assertTrue(result['right_endpoint_checked'])
    def test_non_prime_power_endpoints(self):
        result=certify(260,1050)
        self.assertGreater(result['constant_psi_cells_certified'],0)
    def test_false_envelope_rejected(self):
        with self.assertRaises(ArithmeticError): certify(256,1024,1024)
    def test_wrong_psi_rejected(self):
        with self.assertRaises(ArithmeticError): check_cell(256,257,0,0,16)
    def test_empty_domain_rejected(self):
        with self.assertRaises(ValueError): certify(256,256)
    def test_cubic_identity(self):
        self.assertTrue(exact_identity([1,3,3,1],[1,3,3,1],3,[0,1,2,3]))
    def test_degree_drift_rejected(self):
        # x(x-1)(x-2)(x-3) agrees with zero at 0,1,2,3 but is degree 4.
        with self.assertRaises(ValueError):
            exact_identity([0,-6,11,-6,1],[0],3,[0,1,2,3])
    def test_duplicate_nodes_rejected(self):
        with self.assertRaises(ValueError): exact_identity([0,1],[0,1],1,[0,0])
    def test_identity_mutation_rejected(self):
        self.assertFalse(exact_identity([1,3,3,1],[1,3,4,1],3,[0,1,2,3]))
    def test_divisibility_six_obstruction(self):
        for m in range(1,10001):
            count=(2*m)//6 - m//6
            self.assertGreaterEqual(6*count, m-6)
    def test_runtime_not_output_growth(self):
        n=10000
        # Same loop length/addition count; different cancellation.
        ones=sum(1 for _ in range(n))
        alternating=sum(1 if i%2==0 else -1 for i in range(n))
        self.assertEqual(ones, n)
        self.assertEqual(alternating, 0)


if __name__ == '__main__': unittest.main(verbosity=2)
