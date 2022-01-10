import unittest

from parameterized import parameterized

from challenges.hackerrank.count_triplets import countTriplets


class CountTripletsTests(unittest.TestCase):
    @parameterized.expand(
        [
            (1, [1, 1, 1, 5, 1], 4),
            (1, [1, 1, 1, 5], 1),
            (5, [1, 5, 5, 25, 125], 4),
        ]
    )
    def test_should_count_triplets(self, r, arr, expected_triplets):
        # act
        triplets = countTriplets(arr, r)

        # assert
        self.assertEqual(triplets, expected_triplets)
