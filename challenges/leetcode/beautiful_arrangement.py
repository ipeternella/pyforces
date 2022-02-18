"""
Solution for LC#526: Beautiful Arrangement

https://leetcode.com/problems/beautiful-arrangement/
"""


class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(start, nums):
            nonlocal count

            if start > n:
                count += 1

            for i in range(start, n + 1):
                nums[start], nums[i] = nums[i], nums[start]

                # reduce search space of O(N!): after the traditional permutation swap
                # if the start number of the swap is not divisible: no need to go further!
                if nums[start] % start == 0 or start % nums[start] == 0:
                    backtrack(start + 1, nums)

                nums[start], nums[i] = nums[i], nums[start]

        nums = list(range(n + 1))
        count = 0

        backtrack(1, nums)
        return count
