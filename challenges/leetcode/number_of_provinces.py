"""
Solution for LC#547: Number of Provinces

https://leetcode.com/problems/number-of-provinces/
"""
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            isConnected[i][i] = 2

            for j in range(n):
                if isConnected[i][j] == 1 and isConnected[j][j] != 2:
                    dfs(j)

        n = len(isConnected)
        provinces = 0
        for i in range(n):
            if isConnected[i][i] != 2:  # dfs non-visited nodes
                provinces += 1
                dfs(i)

        return provinces
