"""
Solution for LC#62: Unique Paths

https://leetcode.com/problems/unique-paths/
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                top = dp[i - 1][j] if 0 <= i < m or 0 <= j < n else 0
                left = dp[i][j - 1] if 0 <= i < m or 0 <= j < n else 0
                dp[i][j] = top + left

        return dp[m - 1][n - 1]
