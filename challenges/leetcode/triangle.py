"""
Solution for LC#120: Triangle

https://leetcode.com/problems/triangle/
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[m - 1])

        if m < 2:
            return triangle[0][0]

        state = [[0] * n for _ in range(m)]
        state[0][0] = triangle[0][0]

        for i in range(m - 1):
            cols = len(triangle[i + 1])

            for j in range(cols):
                if j == 0:
                    state[i + 1][j] = state[i][j] + triangle[i + 1][j]
                elif j == cols - 1:
                    state[i + 1][j] = state[i][j - 1] + triangle[i + 1][j]
                else:
                    curr = triangle[i + 1][j]
                    state[i + 1][j] = min(curr + state[i][j - 1], curr + state[i][j])

        return min(state[m - 1])
