import unittest

from parameterized import parameterized

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
