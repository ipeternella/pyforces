"""
Solution for LC#1054: Distant Barcodes

https://leetcode.com/problems/distant-barcodes/
"""
from collections import Counter
from queue import PriorityQueue
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        q = PriorityQueue()  # min. heap under the hood: so negate frequencies to simulate max heap
        shuffled = []

        for code, freq in Counter(barcodes).items():
            q.put((-freq, code))

        while q.qsize() > 1:
            f1, val1 = q.get()
            f2, val2 = q.get()

            # conversion from min heap to max heap
            f1 = -f1 - 1
            f2 = -f2 - 1

            # process
            shuffled.append(val1)
            shuffled.append(val2)

            # added values with one less frequency
            if f1 > 0:
                q.put((-f1, val1))

            if f2 > 0:
                q.put((-f2, val2))

        # deal with final element of the queue if available
        if not q.empty():
            _, val = q.get()
            shuffled.append(val)

        return shuffled
