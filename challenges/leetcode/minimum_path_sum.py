"""
Solution for LC#64: Minimum Path Sum

https://leetcode.com/problems/minimum-path-sum/
"""
import sys
from typing import List

INF = sys.maxsize


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                top = dp[i - 1][j] + grid[i][j] if i - 1 >= 0 else INF
                left = dp[i][j - 1] + grid[i][j] if j - 1 >= 0 else INF
                dp[i][j] = min(top, left)

        return dp[m - 1][n - 1]
