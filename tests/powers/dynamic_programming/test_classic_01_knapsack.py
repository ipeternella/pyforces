import unittest

from parameterized import parameterized

from powers.dynamic_programming.classic_01_knapsack import knapsack_bruteforce
from powers.dynamic_programming.classic_01_knapsack import knapsack_memoized


class Classic01KnapsackTests(unittest.TestCase):
    @parameterized.expand([([30, 50, 60], [3, 4, 5], 8, 90), ([5, 6, 4, 6, 5, 2], [6, 5, 6, 6, 3, 7], 15, 17)])
    def test_should_maximize_knapsack_value(self, values, weights, max_weight, expected_max_knapsack_value):
        # act
        max_knapsack_value = knapsack_bruteforce(values, weights, max_weight)

        # assert
        self.assertEqual(max_knapsack_value, expected_max_knapsack_value)

    @parameterized.expand([([30, 50, 60], [3, 4, 5], 8, 90), ([5, 6, 4, 6, 5, 2], [6, 5, 6, 6, 3, 7], 15, 17)])
    def test_should_maximize_knapsack_value_memoized(self, values, weights, max_weight, expected_max_knapsack_value):
        # act
        max_knapsack_value = knapsack_memoized(values, weights, max_weight)

        # assert
        self.assertEqual(max_knapsack_value, expected_max_knapsack_value)
