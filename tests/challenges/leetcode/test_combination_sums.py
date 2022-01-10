import unittest
from typing import List

from challenges.leetcode.combination_sums import Solution


class HouseRobberTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_should_find_combination_sum(self):
        # arrange
        candidates = [2, 3, 6, 7]
        target = 7

        # act
        combinations: List[List[int]] = self.solution.combinationSum(candidates, target)

        # assert
        self.assertEqual(combinations, [[2, 2, 3], [7]])

    def test_should_find_combination_sum_ii(self):
        # arrange
        candidates = [2, 3, 5]
        target = 8

        # act
        combinations: List[List[int]] = self.solution.combinationSum(candidates, target)

        # assert
        self.assertEqual(combinations, [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
