import unittest

from parameterized import parameterized

from challenges.hackerrank.coin_change_problem import getWays


class CoinChangeProblemTests(unittest.TestCase):
    @parameterized.expand(
        [
            (3, [8, 3, 1, 2], 3),
            (4, [1, 2, 3], 4),
            (10, [2, 5, 3, 6], 5),
        ]
    )
    def test_should_compute_amount_ways_for_coins_change(self, n, c, expected_amount_ways):
        # act
        ways = getWays(n, c)

        # assert
        self.assertEqual(ways, expected_amount_ways)
