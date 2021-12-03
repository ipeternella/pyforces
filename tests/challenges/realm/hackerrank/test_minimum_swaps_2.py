import unittest

from parameterized import parameterized

from challenges.realm.hackerrank.minimum_swaps_2 import minimumSwaps


class MinimumSwapsIITests(unittest.TestCase):
    @parameterized.expand(
        [
            ([3, 2, 1], 1),
            ([3, 2, 1, 0], 2),
            ([1, 3, 5, 2, 4, 6, 7], 3),
        ]
    )
    def test_should_compute_min_swaps(self, arr, expected_min_swaps):
        # act
        min_swaps = minimumSwaps(arr)

        # assert
        self.assertEqual(min_swaps, expected_min_swaps)
