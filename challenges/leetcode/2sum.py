"""
Solution for LC#1: Two Sum

https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        complements = dict()

        for i in range(n):
            complements[target - nums[i]] = i  # store the index as the nums are NOT unique

        for i in range(n):
            if nums[i] in complements and complements[nums[i]] != i:  # can't reuse same num
                return [i, complements[nums[i]]]

        return [-1, -1]
