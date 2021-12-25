"""
Solution for LC#34: Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        s = -1
        e = -1

        def binary_search(i, j):
            nonlocal s, e
            l = i
            r = j

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    if s == -1 and e == -1:
                        s, e = mid, mid
                    elif mid > e:
                        e = mid
                    elif mid < s:
                        s = mid

                    binary_search(mid + 1, j)
                    binary_search(i, mid - 1)
                    return

        binary_search(0, n - 1)
        return [s, e]
