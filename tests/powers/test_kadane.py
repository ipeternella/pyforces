import unittest

from parameterized import parameterized

from powers.kadane import kadane


class RangeUpdatesTests(unittest.TestCase):
    @parameterized.expand(
        [
            ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
            ([-2, -10, 5], 5),
            ([-2, -10, -3], -2),
            ([-2, 1, -3], 1),
            ([-2, 1, 4, -2], 5),
        ]
    )
    def test_should_compute_largest_subarray_sum(self, nums, expected_sum):
        # act
        largest_sum = kadane(nums)

        # assert
        self.assertEqual(largest_sum, expected_sum)
