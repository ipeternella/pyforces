import unittest

from challenges.leetcode.number_of_islands import Solution


class NumberOfIslandsTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_should_find_number_of_islands_i(self):
        # arrange
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]

        # act
        number_of_islands = self.solution.numIslands(grid)

        # assert
        self.assertEqual(number_of_islands, 1)

    def test_should_find_number_of_islands_ii(self):
        # arrange
        grid = grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]

        # act
        number_of_islands = self.solution.numIslands(grid)

        # assert
        self.assertEqual(number_of_islands, 3)
