"""
Solution for LC#1710: Maximum Units on a Truck

https://leetcode.com/problems/maximum-units-on-a-truck/
"""
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes_types = sorted(boxTypes, key=(lambda t: t[1]), reverse=True)
        remaining = truckSize
        units = 0

        # greedy: always go for the boxes with the highest number of units as
        # every box counts a single box for the truck's capacity
        for amount, unit in boxes_types:
            picked = min(amount, remaining)
            remaining -= picked
            units += unit * picked

            if remaining == 0:
                break

        return units
