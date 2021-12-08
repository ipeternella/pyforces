import unittest

from parameterized import parameterized

from challenges.realm.hackerrank.climbing_the_leaderboard import climbingLeaderboard


class ClimbingTheLeaderboardTests(unittest.TestCase):
    @parameterized.expand(
        [
            ([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120], [6, 4, 2, 1]),
        ]
    )
    def test_should_compute_new_leaderboard(self, ranked, player, expected_new_ranks):
        # act
        new_ranks = climbingLeaderboard(ranked, player)

        # assert
        self.assertEqual(new_ranks, expected_new_ranks)
