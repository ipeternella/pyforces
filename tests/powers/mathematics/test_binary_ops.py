import unittest

from parameterized import parameterized

from powers.mathematics.binary_ops import mod_power
from powers.mathematics.binary_ops import multiply
from powers.mathematics.binary_ops import power


class MathBinaryOperationsTests(unittest.TestCase):
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

    @parameterized.expand([(2, 5, 10), (3, 5, 15)])
    def test_should_multiply_a_b(self, a, b, expected_rslt):
        # act
        rslt = multiply(a, b)

        # assert
        self.assertEqual(rslt, expected_rslt)
