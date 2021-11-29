import unittest

from parameterized import parameterized

from challenges.realm.leetcode.combinations import Solution


class JumpGameIITests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand(
        [
            (1, 1, [[1]]),
            (4, 1, [[1], [2], [3], [4]]),
            (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
            (4, 3, [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]),
            (4, 4, [[1, 2, 3, 4]]),
        ]
    )
    def test_should_find_combinations_of_k_elements(self, n, k, expected_combinations):
        # act
        combinations = self.solution.combine(n, k)

        # assert
        self.assertEqual(combinations, expected_combinations)
