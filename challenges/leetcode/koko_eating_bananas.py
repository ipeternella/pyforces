"""
Solution for LC#875: Koko Eating Bananas

https://leetcode.com/problems/koko-eating-bananas/
"""
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def koko_eating_time(piles, k):
            t = 0
            for bananas in piles:
                t += math.ceil(bananas / k)

            return t

        min_k, max_k = 1, max(piles)
        while min_k < max_k:
            mid_k = (min_k + max_k) // 2
            t = koko_eating_time(piles, mid_k)

            if t <= h:  # eating too fast, so t <= h: decrease k
                max_k = mid_k
            else:
                min_k = mid_k + 1  # eating too slow, so t > h: increase k

        return min_k


class SolutionII:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def koko_eating_time(piles, k):
            t = 0
            for bananas in piles:
                t += math.ceil(bananas / k)

            return max(t, h)  # if t < h, than wait until h

        min_k, max_k = 1, max(piles)
        k = max_k
        while min_k <= max_k:
            mid_k = (min_k + max_k) // 2
            t = koko_eating_time(piles, mid_k)

            if t < h:
                max_k = mid_k - 1  # eating too fast: reduce k
            elif t > h:
                min_k = mid_k + 1  # eating too slow: increase k
            else:
                k = mid_k  # tricky: keep reducing k until a minimal value is found
                max_k = mid_k - 1

        return k
