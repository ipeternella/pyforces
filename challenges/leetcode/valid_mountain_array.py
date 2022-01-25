"""
Solution for LC#941: Valid Mountain Array

https://leetcode.com/problems/valid-mountain-array/
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        increased = False
        has_peak = False

        for i in range(n - 1):
            h1, h2 = arr[i], arr[i + 1]
            dh = h2 - h1

            if has_peak:
                if dh >= 0:
                    return False
            elif dh > 0:
                increased = True
            elif dh == 0:
                return False
            elif dh < 0:
                if not increased:  # dh must have been positive (height increase) before having a peak
                    return False
                has_peak = True

        return has_peak
