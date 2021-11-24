import unittest

from powers.sliding_window import max_sum_k


class SlidingWindowTests(unittest.TestCase):
    def test_should_max_sum_k(self):
        # arrange
        nums = [1, 4, 2, 10, 2, 3, 1, 0, 20]

        # act
        max_sum = max_sum_k(nums, 4)

        # assert
        self.assertEqual(max_sum, 24)
