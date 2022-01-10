"""
Solution for LC#495: Teemo Attacking

https://leetcode.com/problems/teemo-attacking/
"""
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        t_poisoned = 0

        for i in range(n - 1):
            t_hit = timeSeries[i]
            t_next_hit = timeSeries[i + 1]

            if t_hit + duration - 1 >= t_next_hit:
                t_poisoned += t_next_hit - t_hit
            else:
                t_poisoned += duration

        t_poisoned += duration
        return t_poisoned
