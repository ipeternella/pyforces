import unittest

from parameterized import parameterized

from challenges.realm.leetcode.flood_fill import SolutionBFS
from challenges.realm.leetcode.flood_fill import SolutionDFS


class FloodFillTests(unittest.TestCase):
    def setUp(self):
        self.solution_dfs = SolutionDFS()
        self.solution_bfs = SolutionBFS()

    @parameterized.expand(
        [
            ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 7, [[7, 7, 7], [7, 7, 0], [7, 0, 1]]),
            ([[0, 0, 0], [0, 0, 0]], 0, 0, 4, [[4, 4, 4], [4, 4, 4]]),
            ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 2, 2, 5, [[1, 1, 1], [1, 1, 0], [1, 0, 5]]),
        ]
    )
    def test_should_flood_image_using_dfs(self, image, sr, sc, new_color, flooded_img):
        # act
        image = self.solution_dfs.floodFill(image, sr, sc, new_color)

        # assert
        self.assertEqual(image, flooded_img)

    @parameterized.expand(
        [
            ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 7, [[7, 7, 7], [7, 7, 0], [7, 0, 1]]),
            ([[0, 0, 0], [0, 0, 0]], 0, 0, 4, [[4, 4, 4], [4, 4, 4]]),
            ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 2, 2, 5, [[1, 1, 1], [1, 1, 0], [1, 0, 5]]),
        ]
    )
    def test_should_flood_image_using_bfs(self, image, sr, sc, new_color, flooded_img):
        # act
        image = self.solution_bfs.floodFill(image, sr, sc, new_color)

        # assert
        self.assertEqual(image, flooded_img)
