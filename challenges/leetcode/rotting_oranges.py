""""
Solution for LC#994: Rotting Oranges

https://leetcode.com/problems/rotting-oranges/
"""
from collections import deque
from typing import Deque
from typing import List
from typing import Tuple


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def in_grid(i, j):
            return (i >= 0 and i < m) and (j >= 0 and j < n)

        def is_good_orange(i, j):
            return grid[i][j] == 1

        def is_rotten(i, j):
            return grid[i][j] == 2

        m = len(grid)
        n = len(grid[0])
        q: Deque[Tuple[int, int, int]] = deque()
        t = 0
        t_max = 0

        # all rotten must go first: good oranges will begin to rot from many rot points at the same time!
        for i in range(m):
            for j in range(n):
                if is_rotten(i, j):
                    q.append((i, j, 0))

        # bfs from rotten oranges to search good ones to rot!
        while q:
            k, l, t = q.popleft()
            adjs = [(k + 1, l), (k - 1, l), (k, l + 1), (k, l - 1)]
            t_max = max(t_max, t)

            for k, l in adjs:
                if in_grid(k, l) and is_good_orange(k, l):
                    q.append((k, l, t + 1))  # +1 minute for each good orange gone bad
                    grid[k][l] = 2  # good gone bad!

        # check if there are any remaining good oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        # can be zero: there was nothing to rot
        return t_max
