"""
Solution for LC#200: Number of Islands

https://leetcode.com/problems/number-of-islands/
"""
from typing import List


def is_island(grid: List[List[str]], i: int, j: int) -> bool:
    return grid[i][j] == "1"


def is_visited(grid: List[List[str]], i: int, j: int) -> bool:
    return grid[i][j] == "X"


def within_grid(i: int, j: int, m: int, n: int) -> bool:
    return 0 <= i < m and 0 <= j < n


def dfs(grid: List[List[str]], i: int, j: int) -> None:
    m = len(grid)
    n = len(grid[0])
    grid[i][j] = "X"  # mark as visited
    adjacents = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]  # all possible ways

    for mark in adjacents:
        next_i, next_j = mark

        if (
            within_grid(next_i, next_j, m, n)
            and is_island(grid, next_i, next_j)
            and is_visited(grid, next_i, next_j) is False
        ):
            dfs(grid, next_i, next_j)


def count_islands(grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    found_islands = 0

    for i in range(0, m):
        for j in range(0, n):
            if is_island(grid, i, j) and is_visited(grid, i, j) is False:
                found_islands += 1
                dfs(grid, i, j)

    return found_islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return count_islands(grid)
