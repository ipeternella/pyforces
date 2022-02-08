"""
Solution for LC#80: Remove Duplicates from Sorted Array II 

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""
import sys
from typing import List

MARK = sys.maxsize


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1
        prev = nums[0]

        for i in range(1, n):
            curr = nums[i]

            # compare curr with prev to see if more than 2 values has occurred
            # if so, mark these values with a MARK to be removed later!
            if prev == curr:
                count += 1
                if count > 2:
                    nums[i] = MARK
            else:
                count = 1

            if nums[i] != MARK:
                prev = curr

        # for each MARK found increase the offset and shift elements left
        offset = 0
        for i in range(n):
            if nums[i] == MARK:
                offset += 1
            else:
                nums[i - offset] = nums[i]

        return n - offset
