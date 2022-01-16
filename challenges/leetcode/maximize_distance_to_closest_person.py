"""
Solution for LC#849: Maximize Distance to Closest Person

https://leetcode.com/problems/maximize-distance-to-closest-person/
"""
import math
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        max_d, d = 0, 0
        starts_zero = seats[0] == 0

        for i in range(n):
            if seats[i] == 1:
                d = d if starts_zero else math.ceil(d / 2)
                max_d = max(max_d, d)
                starts_zero = False
                d = 0
            else:
                d += 1
                if i == n - 1:
                    max_d = max(max_d, d)

        return max_d
