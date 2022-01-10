"""
LeetCode solution for House Robber (LC#198).

https://leetcode.com/problems/house-robber/
"""
from typing import Dict
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return nums[0]

        state = [0] * n
        state[0] = nums[0]
        state[1] = nums[1] if nums[1] > nums[0] else nums[0]

        # can be improved further: as just state i + 1, i and i - 1 are used, the
        # space complexity can be brought down to O(1) instead of O(N) by using vars
        for i in range(1, n - 1):
            # picking state[i]: drop house i + 1, else: keep with house[i - 1] plus this one (i + 1)
            state[i + 1] = max(state[i], state[i - 1] + nums[i + 1])

        return state[n - 1]


class SolutionRecursive:  # non-optimal!
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(i: int, memory: Dict[int, int]) -> int:
            if i in memory:
                return memory[i]

            if i > n - 1:
                return 0

            local_best = nums[i]
            for skip_size in range(2, n - i):
                local_best = max(local_best, helper(i + skip_size, memory) + nums[i])

            memory[i] = local_best
            return memory[i]

        memory: Dict[int, int] = dict()
        rslt = max(helper(0, memory), helper(1, memory))

        return rslt
