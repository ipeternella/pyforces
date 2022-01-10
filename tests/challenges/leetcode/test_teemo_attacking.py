import unittest

from parameterized import parameterized

from challenges.leetcode.teemo_attacking import Solution


class TeemoAttackingTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand(
        [
            ([1, 10, 20], 11, 30),
            ([1, 10, 20], 10, 29),
        ]
    )
    def test_should_compute_poisoned_time(self, time_series, poison_duration, expected_poisoned_time):
        # act
        poisoned_time = self.solution.findPoisonedDuration(time_series, poison_duration)

        # assert
        self.assertEqual(poisoned_time, expected_poisoned_time)
