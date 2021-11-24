"""
Solution for LC#695: Max Area of Island

https://leetcode.com/problems/max-area-of-island/
"""
from collections import deque
from typing import Deque
from typing import List
from typing import Tuple


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def in_grid(i: int, j: int) -> bool:
            return (i < m and i >= 0) and (j < n and j >= 0)

        def is_visited(i: int, j: int) -> bool:
            return grid[i][j] == -1

        def is_island(i: int, j: int) -> bool:
            return grid[i][j] == 1

        def bfs_islands(i: int, j: int) -> int:
            grid[i][j] = -1  # visited
            q.append((i, j))
            size = 1

            while q:
                k, l = q.popleft()
                adj = [(k + 1, l), (k - 1, l), (k, l + 1), (k, l - 1)]

                for k, l in adj:
                    if in_grid(k, l) and not is_visited(k, l) and is_island(k, l):
                        grid[k][l] = -1  # visited
                        size += 1
                        q.append((k, l))

            return size

        m = len(grid)
        n = len(grid[0])
        q: Deque[Tuple[int, int]] = deque()
        max_island_size = 0

        # traverse full grid looking for 1s that have not been visited: new islands
        for i in range(0, m):
            for j in range(0, n):
                if is_island(i, j) and not is_visited(i, j):
                    max_island_size = max(max_island_size, bfs_islands(i, j))

        return max_island_size
