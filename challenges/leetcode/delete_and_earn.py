"""
Solution for LC#740: Delete and Earn

https://leetcode.com/problems/delete-and-earn/
"""

from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        best = 0
        prev_local = 0
        prev_local_2 = 0
        local = 0
        freqs = Counter(nums)

        for num in range(min(freqs), max(freqs) + 1):
            freq = freqs[num]  # freq is zero for non-existent key
            local = prev_local_2 + freq * num

            if local > prev_local:
                prev_local_2 = prev_local
                prev_local = local
                best = max(best, local)
            else:
                prev_local_2 = prev_local

        return best
