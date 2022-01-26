import unittest

from parameterized import parameterized

from powers.bitwise_ops import clear_ith_bit
from powers.bitwise_ops import clear_last_bits
from powers.bitwise_ops import clear_range_bits
from powers.bitwise_ops import count_set_bits
from powers.bitwise_ops import get_ith_bit
from powers.bitwise_ops import int_to_binary
from powers.bitwise_ops import is_odd
from powers.bitwise_ops import is_power_of_two
from powers.bitwise_ops import power
from powers.bitwise_ops import set_ith_bit
from powers.bitwise_ops import update_bit_range
from powers.bitwise_ops import update_ith_bit


class BitwiseOpsTests(unittest.TestCase):
    @parameterized.expand(
        [
            (1, True),
            (2, False),
            (4, False),
            (7, True),
        ]
    )
    def test_should_assert_num_is_odd(self, num, expected_is_odd):
        # act
        is_odd_rslt = is_odd(num)

        # assert
        self.assertEqual(is_odd_rslt, expected_is_odd)

    @parameterized.expand(
        [
            (5, 0, 1),  # 00101
            (5, 1, 0),
            (5, 2, 1),
            (5, 3, 0),
            (5, 4, 0),
        ]
    )
    def test_should_get_ith_bit(self, n, i, expected_ith_bit):
        # act
        ith_bit = get_ith_bit(n, i)

        # assert
        self.assertEqual(ith_bit, expected_ith_bit)

    @parameterized.expand(
        [
            (5, 0, 4),  # 0101
            (5, 2, 1),
            (13, 2, 9),  # 1101
            (13, 1, 13),  # 1101
        ]
    )
    def test_should_clear_ith_bit(self, n, i, expected_num):
        # act
        cleared_num = clear_ith_bit(n, i)

        # assert
        self.assertEqual(cleared_num, expected_num)

    @parameterized.expand(
        [
            (5, 1, 7),  # 0101 (5) -> 0111 (7)
        ]
    )
    def test_should_set_ith_bit(self, n, i, expected_num):
        # act
        num = set_ith_bit(n, i)

        # assert
        self.assertEqual(num, expected_num)

    @parameterized.expand(
        [
            (5, 3, 13, 5),  # 0101 (5) -> 1101 (13), 0101 (5)
            (13, 1, 15, 13),  # 1101 (13) -> 1111 (15), 1101 (13)
            (5, 0, 5, 4),  # 0101 (5) -> 0101 (5), 0100 (4)
            (1, 3, 9, 1),  # 0001 (1) -> 1001 (9), 0001 (1)
        ]
    )
    def test_should_update_ith_bit(self, n, i, expected_set_num, expected_cleared_num):
        # act
        set_num = update_ith_bit(n, i, new_bit=1)
        cleared_num = update_ith_bit(n, i, new_bit=0)

        # assert
        self.assertEqual(set_num, expected_set_num)
        self.assertEqual(cleared_num, expected_cleared_num)

    @parameterized.expand(
        [
            (7, 3, 0),  # 0111 (7)  -> 0000 (0)
            (7, 2, 4),  # 0111 (7)  -> 0100 (4)
            (7, 1, 6),  # 0111 (7)  -> 0110 (6)
            (15, 2, 12),  # 1111 (15)  -> 1100 (12)
        ]
    )
    def test_should_clear_last_bits(self, n, amount, expected_num):
        # act
        cleared_num = clear_last_bits(n, amount)

        # assert
        self.assertEqual(cleared_num, expected_num)

    @parameterized.expand(
        [
            (15, 1, 2, 9),  # 1111 (15)  -> 1001 (9)
            (15, 0, 2, 8),  # 1111 (15)  -> 1000 (8)
            (15, 1, 3, 1),  # 1111 (15)  -> 0001 (1)
            (31, 1, 3, 17),
        ]
    )
    def test_should_clear_range_bits(self, n, i, j, expected_num):
        # act
        cleared_num = clear_range_bits(n, i, j)

        # assert
        self.assertEqual(cleared_num, expected_num)

    @parameterized.expand(
        [
            (15, 1, 3, 2, 5),  # 1111 (15), 010 (2) -> 0101 (5)
        ]
    )
    def test_should_update_bit_range(self, n, i, j, m, expected_num):
        # act
        updated_num = update_bit_range(n, i, j, m)

        # assert
        self.assertEqual(updated_num, expected_num)

    @parameterized.expand(
        [
            (9, 2),  # 1001
            (7, 3),  # 0111
            (2, 1),  # 0010
            (0, 0),  # 0000
        ]
    )
    def test_should_count_set_bits(self, n, expected_set_bits):
        # act
        set_bits = count_set_bits(n)

        # assert
        self.assertEqual(set_bits, expected_set_bits)

    @parameterized.expand(
        [
            (9, False),
            (7, False),
            (0, False),
            (1, True),
            (2, True),
            (16, True),
            (128, True),
            (1024, True),
        ]
    )
    def test_should_find_powers_of_two(self, n, expected_is_power_of_two):
        # act
        is_power = is_power_of_two(n)

        # assert
        self.assertEqual(is_power, expected_is_power_of_two)

    @parameterized.expand(
        [
            (9, 1001),
            (7, 111),
            (5, 101),
            (15, 1111),
        ]
    )
    def test_should_convert_decimal_to_binary(self, n, expected_binary):
        # act
        binary = int_to_binary(n)

        # assert
        self.assertEqual(binary, expected_binary)

    @parameterized.expand([(2, 10, 1024), (3, 5, 243), (5, 5, 3125)])
    def test_should_assert_a_pow_b(self, a, b, expected_a_pow_b):
        # act
        a_pow_b = power(a, b)

        # assert
        self.assertEqual(a_pow_b, expected_a_pow_b)
