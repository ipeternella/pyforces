import unittest

from parameterized import parameterized

from powers.backtrack.subsets_permutations_combinations import subsets


class BacktrackSubsetsTests(unittest.TestCase):
    @parameterized.expand(
        [
            ("abc", ["abc", "ab", "ac", "bc", "c", "a", "b", ""]),
        ]
    )
    def test_should_find_string_subsets(self, s, expected_subsets):
        # act
        computed_subsets = subsets(s)

        # assert
        self.assertCountEqual(computed_subsets, expected_subsets)
