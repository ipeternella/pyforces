"""
Solution for LC#45: Jump Game II

https://leetcode.com/problems/jump-game-ii/
"""
import sys
from typing import List

INF = sys.maxsize


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        # state: dp[i index] = min jumps
        dp = [INF] * n
        dp[0] = 0

        for j in range(n):
            jumps = min(nums[j], n - j - 1)  # clamping, max possible jump size: n - 1 - j
            for jump in range(1, jumps + 1):
                dp[j + jump] = min(dp[j + jump], dp[j] + 1)

        return dp[n - 1]
