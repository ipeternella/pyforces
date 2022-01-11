"""
Solution for LC#1266: Minimum Time Visiting All Points

https://leetcode.com/problems/minimum-time-visiting-all-points/
"""
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        time = 0

        for i in range(n - 1):
            x, y = points[i]
            target_x, target_y = points[i + 1]
            time += max(abs(target_x - x), abs(target_y - y))  # includes diagonal + remaining movements

        return time
