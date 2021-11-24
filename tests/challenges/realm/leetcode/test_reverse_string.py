import unittest

import pytest
from parameterized import parameterized

from challenges.realm.leetcode.reverse_string import Solution


class ReverseStringTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand(
        [
            (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
            (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
            (["h", "i"], ["i", "h"]),
        ]
    )
    def test_should_revert_strings(self, str, expectation):
        # act
        self.solution.reverseString(str)

        # assert
        self.assertEqual(str, expectation)
