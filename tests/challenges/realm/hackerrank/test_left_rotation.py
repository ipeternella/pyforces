import unittest

from parameterized import parameterized

from challenges.realm.hackerrank.left_rotation import rotateLeft


class LeftRotationTests(unittest.TestCase):
    @parameterized.expand(
        [
            (1, [0, 1, 2], [1, 2, 0]),
            (2, [0, 1, 2], [2, 0, 1]),
            (3, [0, 1, 2], [0, 1, 2]),
        ]
    )
    def test_should_left_rotate_arr(self, d, arr, expected_rotated_arr):
        # act
        rotated_arr = rotateLeft(d, arr)

        # assert
        self.assertEqual(rotated_arr, expected_rotated_arr)
