import unittest

from parameterized import parameterized

from challenges.leetcode.permutation_in_string import Solution


class PermutationInStringTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand(
        [
            ("ab", "eidbaooo", True),
            ("abc", "eiaaaadbacoo", True),
            ("abc", "eidbaooo", False),
            ("ab", "a", False),
        ]
    )
    def test_should_check_if_permutations_are_in_string(self, s1, s2, expectation):
        # act
        in_string = self.solution.checkInclusion(s1, s2)

        # assert
        self.assertEqual(in_string, expectation)
