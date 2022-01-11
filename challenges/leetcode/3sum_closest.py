"""
Solution for LC#16: 3Sum Closest

https://leetcode.com/problems/3sum-closest/
"""
import sys
from typing import List

INF = sys.maxsize


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        closest = INF
        closest_dist = INF

        for i in range(n):
            a = nums[i]
            new_target = target - a
            j = i + 1
            k = n - 1

            # pointers which move according to what's needed to
            # reach the new_target as closest as possible
            while j < k:
                b = nums[j]
                c = nums[k]

                if abs(target - (a + b + c)) < closest_dist:
                    closest = a + b + c
                    closest_dist = abs(target - (a + b + c))

                    if closest_dist == 0:  # direct hit to target
                        return a + b + c

                if new_target - (b + c) > 0:
                    j += 1  # need bigger values to reach new_target
                else:
                    k -= 1  # need smaller values to reach new_target

        return closest
