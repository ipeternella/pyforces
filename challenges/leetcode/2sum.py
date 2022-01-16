"""
Solution for LC#1: Two Sum

https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        complements = dict()

        for i in range(n):
            complements[target - nums[i]] = i  # store the index as the nums are NOT unique

        for i in range(n):
            if nums[i] in complements and complements[nums[i]] != i:  # can't reuse same num
                return [i, complements[nums[i]]]

        return [-1, -1]


class SolutionTwoPointers:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        indexes = dict()

        # { num: [i, j, k, ...] }  as nums[i] are NOT unique!
        for i in range(n):
            if nums[i] not in indexes:
                indexes[nums[i]] = [i]
            else:
                indexes[nums[i]].append(i)

        nums = sorted(nums)
        i, j = 0, n - 1
        while i < j:
            two_sum = nums[i] + nums[j]

            if two_sum == target:
                break
            elif two_sum > target:
                j -= 1
            else:
                i += 1

        if nums[i] == nums[j]:  # if both are the same, pick two indexes from same number nums[i] as it repeats!
            return [indexes[nums[i]][0], indexes[nums[i]][1]]

        # nums are different, so pick the first index of nums[i] and nums[j]
        return [indexes[nums[i]][0], indexes[nums[j]][0]]
