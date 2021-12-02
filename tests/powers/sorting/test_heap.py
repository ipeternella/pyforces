import unittest

from parameterized import parameterized

from powers.sorting.heap import heapsort
from powers.sorting.heap import heapsort_builtin
from powers.sorting.heap import heapsort_with_minheap


class HeapSortTests(unittest.TestCase):
    @parameterized.expand(
        [
            ([4, 3, -1, 0, 2], [-1, 0, 2, 3, 4]),
            ([3, 1, 1, 2, 2], [1, 1, 2, 2, 3]),
        ]
    )
    def test_should_sort_numbers(self, nums, expected_sorted_nums):
        # act
        heapsort(nums)  # in-place

        # assert
        self.assertEqual(nums, expected_sorted_nums)

    @parameterized.expand(
        [
            ([4, 3, -1, 0, 2], [-1, 0, 2, 3, 4]),
            ([3, 1, 1, 2, 2], [1, 1, 2, 2, 3]),
        ]
    )
    def test_should_sort_numbers_with_minheap(self, nums, expected_sorted_nums):
        # act
        nums = heapsort_with_minheap(nums)  # returns new list

        # assert
        self.assertEqual(nums, expected_sorted_nums)

    @parameterized.expand(
        [
            ([4, 3, -1, 0, 2], [-1, 0, 2, 3, 4]),
            ([3, 1, 1, 2, 2], [1, 1, 2, 2, 3]),
        ]
    )
    def test_should_sort_numbers_with_builtin_minheap(self, nums, expected_sorted_nums):
        # act
        nums = heapsort_builtin(nums)

        # assert
        self.assertEqual(nums, expected_sorted_nums)
