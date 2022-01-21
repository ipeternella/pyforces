import unittest

from parameterized import parameterized

from powers.binary_search import binary_search


class BinarySearchTests(unittest.TestCase):
    @parameterized.expand(
        [
            ([2, 3, 4, 10, 40], 10, 3),
            ([2, 3, 4, 10, 40], 100, -1),
        ]
    )
    def test_should_binary_search_target_number(self, nums, target, expected_ix):
        # act
        ix = binary_search(nums, target)

        # assert
        self.assertEqual(ix, expected_ix)
