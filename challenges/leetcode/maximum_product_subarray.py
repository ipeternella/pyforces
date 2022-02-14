"""
Solution for LC#152: Maximum Product Subarray

https://leetcode.com/problems/maximum-product-subarray/
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_prod, max_prod = nums[0], nums[0]
        largest = max_prod

        for i in range(1, n):
            # neg number: product changes from min to max and vice-versa
            if nums[i] < 0:
                min_prod, max_prod = max_prod, min_prod

            # max: bigger product value or start over at nums[i]
            # min: smaller product value or start over at nums[i]
            max_prod = max(nums[i], nums[i] * max_prod)
            min_prod = min(nums[i], nums[i] * min_prod)

            # like Kedane's algorithm: always store global max
            largest = max(largest, max_prod)

        return largest
