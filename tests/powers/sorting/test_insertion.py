import unittest

from parameterized import parameterized

from powers.sorting.insertion import insertionsort


class InsertionSortTests(unittest.TestCase):
    @parameterized.expand(
        [
            ([4, 3, -1, 0, 2], [-1, 0, 2, 3, 4]),
            ([3, 1, 1, 2, 2], [1, 1, 2, 2, 3]),
        ]
    )
    def test_should_sort_numbers(self, nums, expected_sorted_nums):
        # act
        sorted_nums = insertionsort(nums)

        # assert
        self.assertEqual(sorted_nums, expected_sorted_nums)
