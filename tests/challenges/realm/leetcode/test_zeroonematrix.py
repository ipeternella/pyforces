import unittest

from parameterized import parameterized

from challenges.realm.leetcode.zeroone_matrix import Solution


class ZeroOneTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand(
        [
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
            ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]),
            ([[1, 0, 0, 1, 0]], [[1, 0, 0, 1, 0]]),
        ]
    )
    def test_should_find_nearest_dist_to_zeros(self, matrix, expected_matrix_dists):
        # act
        matrix_dists = self.solution.updateMatrix(matrix)

        # assert
        self.assertEqual(matrix_dists, expected_matrix_dists)
