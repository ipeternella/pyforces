"""
Solution for LC#18: 4Sum

https://leetcode.com/problems/4sum/
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        quadruplets = set()

        for i in range(n):
            target_3sum = target - nums[i]

            for j in range(i + 1, n):
                target_2sum = target_3sum - nums[j]

                # two pointers technique
                l = j + 1
                r = n - 1
                while l < r:
                    if nums[l] + nums[r] == target_2sum:
                        quadruplets.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > target_2sum:
                        r -= 1
                    else:
                        l += 1

        return quadruplets  # type: ignore
