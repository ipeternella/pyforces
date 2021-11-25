"""
Solution for LC#45: Jump Game II

https://leetcode.com/problems/jump-game-ii/
"""
import sys
from typing import List

INF = sys.maxsize


class SolutionDP:
    """
    [!]: This is not an optimal solution yet: there's a greedy approach which naturally
         is much faster than a tabulated DP approach.
    """

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        dp = [INF] * n
        dp[n - 1] = 0
        dp[n - 2] = 1

        for i in range(n - 3, -1, -1):
            max_jump_size = nums[i]
            for jump_size in range(max_jump_size, 0, -1):

                if i + jump_size <= n - 1:
                    dp[i] = min(dp[i], dp[i + jump_size] + 1)

        return dp[0]
