import unittest

from parameterized import parameterized

from powers.math.binary_exponentiation import mod_power
from powers.math.binary_exponentiation import power


class MathBinaryExponentiationTests(unittest.TestCase):
    @parameterized.expand(
        [
            (2, 5, 32),
            (3, 5, 243),
            (5, 3, 125),
        ]
    )
    def test_should_compute_power_of_a_b(self, a, b, expected_power):
        # act
        rslt = power(a, b)

        # assert
        self.assertEqual(rslt, expected_power)

    @parameterized.expand(
        [
            (2, 200, 10**9 + 7, 499445072),
        ]
    )
    def test_should_compute_power_of_a_b_with_mod(self, a, b, prime, expected_power):
        # act
        rslt = mod_power(a, b, prime)

        # assert
        self.assertEqual(rslt, expected_power)
