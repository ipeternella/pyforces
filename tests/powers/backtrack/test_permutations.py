import unittest

from parameterized import parameterized

from powers.backtrack.subsets_permutations_combinations import permutations


class BacktrackPermutationsTests(unittest.TestCase):
    @parameterized.expand(
        [
            ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
        ]
    )
    def test_should_compute_largest_subarray_sum(self, s, expected_permutations):
        # act
        computed_permutations = permutations(s)

        # assert
        self.assertCountEqual(computed_permutations, expected_permutations)
