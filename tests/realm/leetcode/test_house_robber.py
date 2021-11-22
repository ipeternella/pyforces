import unittest

from challenges.realm.leetcode.house_robber import Solution


class HouseRobberTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_should_compute_max_money(self):
        # arrange
        nums = [1, 2, 3, 1]

        # act
        max_money = self.solution.rob(nums)

        # assert
        self.assertEqual(max_money, 4)

    def test_should_compute_max_money_ii(self):
        # arrange
        nums = [2, 7, 9, 3, 1]

        # act
        max_money = self.solution.rob(nums)

        # assert
        self.assertEqual(max_money, 12)
