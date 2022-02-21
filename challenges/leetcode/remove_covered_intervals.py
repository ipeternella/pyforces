"""
Solution for LC#1288: Remove Covered Intervals

https://leetcode.com/problems/remove-covered-intervals/
"""
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals = sorted(intervals, key=lambda pair: pair[0])
        l_ref, r_ref = intervals[0]
        amount = n

        for i in range(1, n):
            l, r = intervals[i]

            if l >= l_ref and r <= r_ref:  # curr interval is smaller than reference: remove covered range
                amount -= 1
            elif l == l_ref and r > r_ref:  # curr interval is bigger than ref: keep the bigger and update ref!
                amount -= 1
                l_ref, r_ref = l, r
            else:
                l_ref, r_ref = l, r  # curr interval is NOT covered by the ref: update the ref as ranges are sorted!

        return amount
