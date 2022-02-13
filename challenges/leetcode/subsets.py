"""
Solution for LC#78: Subsets

https://leetcode.com/problems/subsets/
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            if start > n - 1:
                subsets.append(subset.copy())
                return

            # path 1: pick the item
            subset.append(nums[start])
            backtrack(start + 1, subset)

            # path 2: backtrack and do not pick the item
            subset.pop()
            backtrack(start + 1, subset)

        n = len(nums)
        subsets = []

        # to generate subsets: either pick the item or not: 2^n possibilities
        backtrack(0, [])
        return subsets
