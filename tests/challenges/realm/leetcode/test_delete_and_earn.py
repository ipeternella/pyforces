import unittest

from parameterized import parameterized

from challenges.realm.leetcode.delete_and_earn import Solution


class JumpGameIITests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand(
        [
            ([3, 4, 2], 6),
            ([2, 2, 3, 3, 3, 4], 9),
            ([2, 2, 3, 3, 3, 4, 6, 6, 7], 21),
        ]
    )
    def test_should_delete_and_earn_maximum_points(self, nums, expected_max_points):
        # act
        max_points = self.solution.deleteAndEarn(nums)

        # assert
        self.assertEqual(max_points, expected_max_points)
