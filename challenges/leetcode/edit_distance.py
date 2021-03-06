"""
Solution for LC#72: Edit Distance

https://leetcode.com/problems/edit-distance/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # dp[m][n] = edit_dist

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    # if one of the sizes are 0 then all the amount of remaining chars is the edit dist
                    dp[i][j] = j if i == 0 else i
                elif word1[i - 1] == word2[j - 1]:
                    # same char, just go on
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # chars are diff: take minimum edit of add, remove or replace plus the current op
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        return dp[m][n]


class SolutionMemoized:
    def minDistance(self, word1: str, word2: str) -> int:
        def levenshtein(m, n, dp):
            # if the other string is empty: return the cost of adding remaining chars: return m or n
            if m == 0 or n == 0:
                return n if m == 0 else m

            if dp[m][n] != -1:
                return dp[m][n]

            # same char, no cost: keep going
            if word1[m - 1] == word2[n - 1]:
                return levenshtein(m - 1, n - 1, dp)

            # levenshtein distance allows: addition, removal and replacement of chars on str1!
            add_cost = levenshtein(m, n - 1, dp)  # add char to str1
            remove_cost = levenshtein(m - 1, n, dp)  # remove char from str1
            replace_cost = levenshtein(m - 1, n - 1, dp)  # replace char on str1 and keep going

            dp[m][n] = min(remove_cost, replace_cost, add_cost) + 1  # current op cost plus remainders
            return dp[m][n]

        m = len(word1)
        n = len(word2)

        dp = [[-1] * (n + 1) for _ in range(m + 1)]  # levenshtein(m, n) has overlapping problems -> memo it!
        return levenshtein(m, n, dp)
