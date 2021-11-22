"""
LeetCode solution for House Robber (LC#198).

https://leetcode.com/problems/house-robber/

Topics: Dynamic programming
"""

from typing import Dict
from typing import List


class Solution:
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
