import unittest

from parameterized import parameterized

from powers.sorting.merge import merge_sorted_subarrays
from powers.sorting.merge import mergesort


class MergeSortTests(unittest.TestCase):
    @parameterized.expand(
        [
            ([2, 4, 5, 7, 1, 2, 3, 6], 0, 3, 7, [1, 2, 2, 3, 4, 5, 6, 7]),
        ]
    )
    def test_should_merge_sorted_subarrays(self, arr, p, q, r, expected_merge_arr):
        # act
        merge_sorted_subarrays(arr, p, q, r)

        # assert
        self.assertEqual(arr, expected_merge_arr)

    @parameterized.expand(
        [
            ([2, 4, 5, 7, 1, 2, 3, 6], [1, 2, 2, 3, 4, 5, 6, 7]),
        ]
    )
    def test_should_sort_array(self, arr, expected_sorted_arr):
        # act
        mergesort(arr)

        # assert
        self.assertEqual(arr, expected_sorted_arr)
