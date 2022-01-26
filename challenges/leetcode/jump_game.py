"""
Solution for LC#55: Jump Game

https://leetcode.com/problems/jump-game/
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        needed = 0

        if n < 2:
            return True

        for i in range(n - 2, -1, -1):
            if needed > 0:
                if nums[i] < needed:
                    needed += 1
                else:
                    needed = 0

            else:  # needed <= 0
                if nums[i] == 0:
                    needed = 2

        return needed <= 0
