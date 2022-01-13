"""
Solution for LC#452: Minimum Number of Arrows to Burst Balloons

https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points = sorted(points, key=(lambda pair: pair[0]))
        arrows = 1
        intersection = points[0]

        for i in range(1, n):
            pair = points[i]

            if pair[0] >= intersection[0] and pair[0] <= intersection[1]:
                # reuse same arrow: no increasing
                intersection = [max(intersection[0], pair[0]), min(intersection[1], pair[1])]
            else:
                arrows += 1
                intersection = pair

        return arrows
