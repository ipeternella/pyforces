"""
Solution for LC#733: Flood Fill

https://leetcode.com/problems/flood-fill/
"""
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def in_image(i, j):
            return (i < m and i >= 0) and (j < n and j >= 0)

        def dfs_flood(i, j, target):
            image[i][j] = newColor
            adj = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

            for row, col in adj:
                # not visited: image[row][col] != newColor
                if in_image(row, col) and image[row][col] != newColor and image[row][col] == target:
                    image[row][col] = newColor
                    dfs_flood(row, col, target)

        m = len(image)
        n = len(image[0])

        dfs_flood(sr, sc, image[sr][sc])
        return image
