import unittest

from parameterized import parameterized

from powers.backtrack.permutations import find_permutations


class BacktrackPermutationsTests(unittest.TestCase):
    @parameterized.expand(
        [
            ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
        ]
    )
    def test_should_compute_largest_subarray_sum(self, s, expected_permutations):
        # act
        permutations = find_permutations(s)

        # assert
        self.assertCountEqual(permutations, expected_permutations)
