"""
Solution for LeetCode: Combination Sums (LC#39).

https://leetcode.com/problems/combination-sum/
"""


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []

        def backtrack(candidates: List[int], target: int, start: int = 0, local: List[int] = list()) -> None:
            if target == 0:
                solutions.append(local.copy())
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                local.append(candidates[i])
                backtrack(candidates, target - candidates[i], i, local)
                local.pop()

        backtrack(candidates, target, 0, [])
        return solutions
