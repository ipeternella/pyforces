"""
Solution for LC#1143: Longest Common Subsequence

https://leetcode.com/problems/longest-common-subsequence/
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


class SolutionMemoized:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(m, n, dp):
            if m == 0 or n == 0:
                return 0  # no common char

            if dp[m][n] != -1:
                return dp[m][n]

            if text1[m - 1] == text2[n - 1]:
                return lcs(m - 1, n - 1, dp) + 1

            dp[m][n] = max(lcs(m - 1, n, dp), lcs(m, n - 1, dp))
            return dp[m][n]

        m = len(text1)
        n = len(text2)

        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        return lcs(m, n, dp)
