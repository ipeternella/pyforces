"""
Solution for LC#46: Permutations

https://leetcode.com/problems/permutations/
"""
from typing import List
from typing import Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []

        def backtrack_permutations(permutation: List[int], picked: Set[int]) -> None:
            if len(picked) == n:
                permutations.append(permutation.copy())
                return

            for i in range(n):
                if nums[i] not in picked:
                    permutation.append(nums[i])
                    picked.add(nums[i])
                    backtrack_permutations(permutation, picked)
                    permutation.pop()
                    picked.remove(nums[i])

        backtrack_permutations([], set())
        return permutations
