"""
Solution for LC#238: Product of Array Except Self

https://leetcode.com/problems/product-of-array-except-self/
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = nums
        n = len(a)
        results = [1] * n
        prefixes = [1] * n
        suffixes = [1] * n

        prefixes[0] = nums[0]
        suffixes[n - 1] = nums[n - 1]

        for i in range(1, n):
            prefixes[i] = a[i] * prefixes[i - 1]

        for i in range(n - 2, -1, -1):
            suffixes[i] = a[i] * suffixes[i + 1]

        for i in range(n):
            prefix = prefixes[i - 1] if i > 0 else 1
            suffix = suffixes[i + 1] if i < n - 1 else 1
            results[i] = prefix * suffix

        return results
