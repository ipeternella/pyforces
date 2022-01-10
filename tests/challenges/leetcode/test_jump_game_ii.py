import unittest

from parameterized import parameterized

from challenges.leetcode.jump_game_ii import SolutionDP


class JumpGameIITests(unittest.TestCase):
    def setUp(self):
        self.solution = SolutionDP()

    @parameterized.expand(
        [
            ([1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1], 4),
            ([2, 3, 1, 1, 4], 2),
            ([2, 3, 0, 1, 4], 2),
            ([1, 2], 1),
            ([0], 0),
        ]
    )
    def test_should_find_min_jumps(self, nums, expected_min_jumps):
        # act
        min_jumps = self.solution.jump(nums)

        # assert
        self.assertEqual(min_jumps, expected_min_jumps)
