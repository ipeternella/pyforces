import unittest

from parameterized import parameterized

from challenges.leetcode.climbing_stairs import Solution


class ClimbingStairsTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([(2, 2), (3, 3), (1, 1), (37, 39088169)])
    def test_should_count_ways_to_the_top(self, steps, expected_ways):
        # act
        ways = self.solution.climbStairs(steps)

        # assert
        self.assertEqual(ways, expected_ways)
