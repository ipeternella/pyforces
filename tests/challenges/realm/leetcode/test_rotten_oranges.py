import unittest

from parameterized import parameterized

from challenges.realm.leetcode.rotten_oranges import Solution


class RottenOrangesTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand(
        [
            ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
            ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
            ([[2, 1, 1], [1, 1, 1], [1, 1, 2]], 2),  # TWO rotting points at the same time!
            ([[1, 0, 2, 1]], -1),  # never rots
            ([[0, 2, 2]], 0),  # nothing to rot
        ]
    )
    def test_should_remove_nth_node_from_linkedlist(self, grid, expected_minutes_to_rot):
        # act
        minutes_to_rot = self.solution.orangesRotting(grid)

        # assert
        self.assertEqual(minutes_to_rot, expected_minutes_to_rot)
