import unittest

from parameterized import parameterized

from challenges.realm.hackerrank.balanced_brackets import isBalanced


class BalancedBracketsTests(unittest.TestCase):
    @parameterized.expand(
        [
            (r"{{[[(())]]}}", True),
            (r"{[(])}", False),
            (r"{[", False),
        ]
    )
    def test_should_compute_new_leaderboard(self, s, expected_is_balanced):
        # act
        is_balanced = isBalanced(s)

        # assert
        self.assertEqual(is_balanced, expected_is_balanced)
