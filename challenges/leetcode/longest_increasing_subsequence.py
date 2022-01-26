"""
Solution for LC#300: Longest Increasing Subsequence

https://leetcode.com/problems/longest-increasing-subsequence/
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n)
        dp[0] = 1

        for i in range(1, n):
            lis = 0
            for j in range(i):
                # when nums[i] > nums[j], nums[i] can be at the end of the subsequence
                # so pick the longest length so far and add 1
                if nums[i] > nums[j]:
                    lis = max(lis, dp[j])

            dp[i] = lis + 1

        return max(dp)
