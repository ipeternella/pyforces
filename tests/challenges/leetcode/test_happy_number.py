import unittest

from parameterized import parameterized

from challenges.leetcode.happy_number import Solution


class HappyNumberTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand([(19, True), (15, False), (2, False)])
    def test_should_check_for_happy_number(self, n, expected_is_happy):
        # act
        is_happy = self.solution.isHappy(n)

        # assert
        self.assertEqual(is_happy, expected_is_happy)
