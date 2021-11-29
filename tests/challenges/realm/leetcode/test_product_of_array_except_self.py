import unittest

from parameterized import parameterized

from challenges.realm.leetcode.product_of_array_except_self import Solution


class ProductOfArrayExceptSelfTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @parameterized.expand(
        [
            ([1, 2, 3, 4], [24, 12, 8, 6]),
            ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
            ([0, 7], [7, 0]),
        ]
    )
    def test_should_find_products(self, nums, expected_products_except_self):
        # act
        products_except_self = self.solution.productExceptSelf(nums)

        # assert
        self.assertEqual(products_except_self, expected_products_except_self)
