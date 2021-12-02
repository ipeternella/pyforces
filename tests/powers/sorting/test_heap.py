import unittest

from parameterized import parameterized

from powers.sorting.heap import heapsort


class HeapSortTests(unittest.TestCase):
    @parameterized.expand(
        [
            ([4, 3, -1, 0, 2], [-1, 0, 2, 3, 4]),
            ([3, 1, 1, 2, 2], [1, 1, 2, 2, 3]),
        ]
    )
    def test_should_sort_numbers(self, nums, expected_sorted_nums):
        # act
        heapsort(nums)

        # assert
        self.assertEqual(nums, expected_sorted_nums)
