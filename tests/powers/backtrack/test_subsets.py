import unittest

from parameterized import parameterized

from powers.backtrack.subsets import find_subsets


class BacktrackSubsetsTests(unittest.TestCase):
    @parameterized.expand(
        [
            ("abc", ["abc", "ab", "ac", "bc", "c", "a", "b", ""]),
        ]
    )
    def test_should_compute_largest_subarray_sum(self, s, expected_subsets):
        # act
        subsets = find_subsets(s)

        # assert
        self.assertCountEqual(subsets, expected_subsets)
