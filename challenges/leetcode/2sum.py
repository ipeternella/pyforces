"""
Solution for LC#1: Two Sum

https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        complements = dict()
        pair_2sum = []

        # store two sum complement of each number: trade memory to reduce O(N^2) runtime
        for i in range(n):
            complements[target - nums[i]] = i

        # O(N) in time, O(N) in space
        for i in range(n):
            if nums[i] in complements:
                j = complements[nums[i]]

                if j > i:  # complement must always be ahead to avoid duplicates
                    pair_2sum = [i, j]
                    break

        return pair_2sum


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
