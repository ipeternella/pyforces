"""
Solution for LC#134: Gas Station

https://leetcode.com/problems/gas-station/
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start, i = 0, 0
        while start < n:
            tank = 0
            has_circle = False
            i = start

            while True:
                if i == start and has_circle:
                    return start

                tank += gas[i] - cost[i]

                # can't proceed further
                if tank < 0:
                    i += 1
                    start = i if i > start else start + 1
                    break

                # proceed further with circular movement
                i += 1
                if i > n - 1:
                    has_circle = True
                    i = i % n

        return -1
