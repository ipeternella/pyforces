"""
Module with binary search implementations.

[!]: Keep in mind that binary search can be applied to ANY monotonic increasing or
     decreasing SEARCH SPACES. As a consequence, many problems may require binary
     searching variables or quantities and not key values in an array. In such cases,
     it may not be so trivial to see that binary searching is required to efficiently
     solve the problem.
"""
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            # this part can be changed to find upper and lower bounds
            # by keep binary searching on left/right subarrays
            l = mid + 1

    return -1
