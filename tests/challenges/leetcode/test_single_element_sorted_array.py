import unittest

from challenges.leetcode.single_element_sorted_array import Solution


class HouseRobberTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_should_find_single_element(self):
        # arrange
        nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

        # act
        single = self.solution.singleNonDuplicate(nums)

        # assert
        self.assertEqual(single, 2)

    def test_should_find_single_element_ii(self):
        # arrange
        nums = [3, 3, 7, 7, 10, 11, 11]

        # act
        single = self.solution.singleNonDuplicate(nums)

        # assert
        self.assertEqual(single, 10)
