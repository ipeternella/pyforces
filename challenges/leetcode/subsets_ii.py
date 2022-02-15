"""
Solution for LC#90: Subsets II

https://leetcode.com/problems/subsets-ii/
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            if start > n - 1:
                subsets.add(tuple(sorted(subset)))
                return

            # pick item
            subset.append(nums[start])
            backtrack(start + 1, subset)

            # backtrack and do not pick the item -> O(2^N)
            subset.pop()
            backtrack(start + 1, subset)

        subsets = set()
        n = len(nums)

        backtrack(0, [])
        return subsets  # type: ignore
