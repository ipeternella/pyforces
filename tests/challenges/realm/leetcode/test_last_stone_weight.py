import unittest

from parameterized import parameterized

from challenges.realm.leetcode.last_stone_weight import Solution


class LastStoneWeightTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([([2, 7, 4, 1, 8, 1], 1), ([1], 1), ([3, 7, 8], 2)])
    def test_should_get_smallest_weight(self, stones, expected_smallest_weight):
        # act
        smallest_weight = self.solution.lastStoneWeight(stones)

        # assert
        self.assertEqual(smallest_weight, expected_smallest_weight)
