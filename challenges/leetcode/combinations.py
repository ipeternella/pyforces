"""
Solution for LC#77: Combinations

https://leetcode.com/problems/combinations/
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs: List[List[int]] = []

        def backtrack_combinations(start: int, comb: List[int]):
            if len(comb) >= k:
                combs.append(comb.copy())
                return

            for other in range(start, n + 1):
                comb.append(other)
                backtrack_combinations(other + 1, comb)
                comb.pop()  # backtrack

        backtrack_combinations(1, [])
        return combs
