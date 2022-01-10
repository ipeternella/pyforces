"""
Solution for LC#47: Permutations II

https://leetcode.com/problems/permutations-ii/
"""
from typing import List
from typing import Set
from typing import Tuple


class Solution:
    def permuteUnique(self, nums: List[int]) -> Set[Tuple[int, ...]]:
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def permute(start: int) -> None:
            if start == n:
                results.add(tuple(nums))

            for i in range(start, n):
                swap(nums, start, i)
                permute(start + 1)
                swap(nums, start, i)

        n = len(nums)
        results: Set[Tuple[int, ...]] = set()
        permute(0)

        return results
