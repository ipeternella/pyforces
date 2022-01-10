"""
Solution for LC#1046: Last Stone Weight

https://leetcode.com/problems/last-stone-weight/
"""
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap: List[int] = []

        # python's heapq is a min heap, negative it to "emulate" a max heap
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            stone1, stone2 = -heapq.heappop(heap), -heapq.heappop(heap)  # back to positive
            result = 0

            if stone1 > stone2:
                result = stone1 - stone2

            if stone1 < stone2:
                result = stone2 - stone1

            if result != 0:
                heapq.heappush(heap, -result)

        if not heap:
            return 0

        return -heapq.heappop(heap)
