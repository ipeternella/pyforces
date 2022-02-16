"""
Solution for LC#15: 3Sum

https://leetcode.com/problems/3sum/
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = set()
        prev_target_2sum = set()

        for i in range(n):
            target_2sum = -nums[i]
            complements = dict()

            # avoid working on previous 2sum targets
            if target_2sum not in prev_target_2sum:
                for j in range(i + 1, n):
                    complements[target_2sum - nums[j]] = j

                for j in range(i + 1, n):
                    if nums[j] in complements:
                        k = complements[nums[j]]

                        if k != j:  # number cannot complement itself (that's why we store indexes in complements)
                            triplet = sorted([nums[i], nums[j], nums[k]])
                            triplets.add(tuple(triplet))

                prev_target_2sum.add(target_2sum)

        return triplets  # type: ignore
