import unittest

from parameterized import parameterized

from challenges.leetcode.letter_case_permutation import Solution


class LetterCasePermutationTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand(
        [
            ("a1b2", ["A1B2", "A1b2", "a1B2", "a1b2"]),
            ("3z4", ["3Z4", "3z4"]),
            ("12345", ["12345"]),
            ("0", ["0"]),
        ]
    )
    def test_should_get_all_case_permutated_strings(self, s, expected_case_permutations):
        # act
        case_permutations = self.solution.letterCasePermutation(s)

        # assert
        self.assertEqual(case_permutations, expected_case_permutations)
