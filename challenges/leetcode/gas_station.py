"""
Solution for LC#134: Gas Station

https://leetcode.com/problems/gas-station/
"""
from collections import deque as Queue
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        q: Queue[int] = Queue()
        for i in range(n):
            if gas[i] >= cost[i]:
                q.append(i)

        min_start = -1
        while q:
            start = q.popleft()
            tank = 0
            i = start
            has_circle = False

            if start < min_start:
                continue

            # circular moving algorithm
            while True:
                if i == start and has_circle:
                    return start

                tank += gas[i]
                tank -= cost[i]

                # can't proceed further
                if tank < 0:
                    min_start = i + 1
                    break  # impossible

                # proceed further with circular movement
                i += 1
                if i > n - 1:
                    has_circle = True
                    i = i % n

        return -1
