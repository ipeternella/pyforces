import unittest

from parameterized import parameterized

from challenges.realm.leetcode.triangle import Solution


class TriangleTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand(
        [
            ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
            ([[2], [3, 4], [6, 5, 7], [100, 50, 8, 3]], 16),
            ([[-10]], -10),
        ]
    )
    def test_should_minimize_path_sum_top_bottom(self, triangle, expected_min_sum):
        # act
        min_sum = self.solution.minimumTotal(triangle)

        # assert
        self.assertEqual(min_sum, expected_min_sum)
