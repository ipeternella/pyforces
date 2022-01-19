"""
Solution for LC#118: Pascal's Triangle

https://leetcode.com/problems/pascals-triangle/
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0] * i for i in range(1, numRows + 1)]

        for row in range(numRows):
            size = row + 1
            for i in range(size):
                if i == 0 or i == size - 1:
                    dp[row][i] = 1
                else:
                    dp[row][i] = dp[row - 1][i - 1] + dp[row - 1][i]

        return dp
