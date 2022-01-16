import unittest

from parameterized import parameterized

from powers.two_pointers import find_subarray_sums


class TwoPointersTests(unittest.TestCase):
    @parameterized.expand(
        [
            ([1, 3, 2, 5, 1, 1, 1, 3], 8, [(2, 4), (3, 6)]),
            ([8, 2, 5, 1], 8, [(0, 0), (1, 3)]),
            ([8, 2, 10, 15, 20, 30, 8], 8, [(0, 0), (6, 6)]),
            ([], 8, []),
            ([8], 8, [(0, 0)]),
            ([10], 8, []),
        ]
    )
    def test_should_find_subarray_sums(self, nums, target, expected_subarrays):
        # act
        subarrays = find_subarray_sums(nums, target)

        # assert
        self.assertEqual(subarrays, expected_subarrays)
