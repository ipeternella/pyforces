import unittest

from parameterized import parameterized

from challenges.leetcode.max_area_of_island import Solution


class MaxAreaOfIslandTests(unittest.TestCase):
    def setUp(self):
        self.solution_bfs = Solution()

    @parameterized.expand(
        [
            (
                [
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                ],
                6,
            ),
            (
                [
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                ],
                16,
            ),
            ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),
        ]
    )
    def test_should_flood_image_using_dfs(self, map_grid, expected_max_size):
        # act
        max_island_size = self.solution_bfs.maxAreaOfIsland(map_grid)

        # assert
        self.assertEqual(max_island_size, expected_max_size)
