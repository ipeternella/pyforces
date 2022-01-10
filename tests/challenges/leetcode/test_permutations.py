import unittest

from parameterized import parameterized

from challenges.leetcode.permutations import Solution


class PermutationTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand(
        [
            ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
            ([0, 1], [[0, 1], [1, 0]]),
            ([1], [[1]]),
        ]
    )
    def test_should_find_permutations(self, nums, expected_permutations):
        # act
        permutations = self.solution.permute(nums)

        # assert
        self.assertEqual(permutations, expected_permutations)
