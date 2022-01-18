"""
Solution for LC#605: Can Place Flowers

https://leetcode.com/problems/can-place-flowers/
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        free_behind, free_ahead = True, True
        capacity = 0

        for i in range(m):
            if flowerbed[i] == 1:  # not a free spot
                continue

            free_behind = flowerbed[i - 1] == 0 if i - 1 >= 0 else True
            free_ahead = flowerbed[i + 1] == 0 if i + 1 < m else True

            if free_behind and free_ahead:
                capacity += 1
                flowerbed[i] = 1  # not free anymore

        return n <= capacity
