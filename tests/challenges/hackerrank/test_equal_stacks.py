import unittest

from parameterized import parameterized

from challenges.hackerrank.equal_stacks import equalStacks


class EqualStacksTests(unittest.TestCase):
    @parameterized.expand([([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1], 5)])
    def test_should_compute_max_height(self, h1, h2, h3, expected_max_height):
        # act
        max_height = equalStacks(h1, h2, h3)

        # assert
        self.assertEqual(max_height, expected_max_height)
