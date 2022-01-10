"""
Solution for LC#46: Permutations

https://leetcode.com/problems/permutations/
"""
from typing import List
from typing import Set


class SolutionII:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def permute(start: int) -> None:
            if start == n:
                results.append(nums.copy())

            for i in range(start, n):
                swap(nums, start, i)
                permute(start + 1)
                swap(nums, start, i)

        n = len(nums)
        results: List[List[int]] = []
        permute(0)

        return results


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
