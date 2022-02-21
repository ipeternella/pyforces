"""
Solution for LC#169: Majority Element

https://leetcode.com/problems/majority-element/
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore voting algorithm
        n = len(nums)
        count = 1
        candidate = nums[0]

        for i in range(1, n):
            count = count + 1 if nums[i] == candidate else count - 1

            # if count reaches <= zero: pick a new majority candidate
            # as eventually the majority candidate will appear more so
            # previous prefixes can be safely discarded
            if count <= 0:
                candidate = nums[i]
                count = 1

        return candidate
