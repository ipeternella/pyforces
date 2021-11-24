import unittest

from powers.range_update_lists import apply_range_updates
from powers.range_update_lists import diff_list
from powers.range_update_lists import range_update


class RangeUpdatesTests(unittest.TestCase):
    def test_should_compute_diff_lists(self):
        # arrange
        nums = [1, 5, 3]

        # act
        diff = diff_list(nums)

        # assert
        self.assertEqual(diff, [1, 4, -2, 0])

    def test_should_perform_range_updates(self):
        # arrange
        nums = [1, 5, 3]
        diffs = diff_list(nums)

        # act - apply increments to [L, R] ranges (inclusive)
        range_update(diffs, 0, 1, 10)
        apply_range_updates(nums, diffs)

        # assert
        self.assertEqual(nums, [11, 15, 3])
