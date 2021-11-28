"""
Solution for LC#542: 01 Matrix

https://leetcode.com/problems/01-matrix/
"""
import sys
from collections import deque
from typing import Deque
from typing import List
from typing import Tuple

INF = sys.maxsize


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def in_grid(i, j):
            return (i >= 0 and i < m) and (j >= 0 and j < n)

        a = mat
        m = len(a)
        n = len(a[0])
        q: Deque[Tuple[int, int]] = deque()

        # enqueues zeros and swaps 1s for INFs for the min. distances to work
        for i in range(m):
            for j in range(n):
                if a[i][j] == 0:
                    a[i][j] = 0
                    q.append((i, j))  # enqueues zeros
                else:
                    a[i][j] = INF

        while q:
            i, j = q.popleft()  # starts with zeros
            adjs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

            for k, l in adjs:
                # if a[i][j] + 1 can 'offer' a smaller value, set it to the adjacent cell
                # and by smaller value it means a shorter distance to a zero
                if in_grid(k, l) and a[i][j] + 1 < a[k][l]:
                    q.append((k, l))
                    a[k][l] = a[i][j] + 1

        return a
