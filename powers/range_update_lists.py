"""
Technique used to perform array queries in O(1) time complexity based
on difference arrays (lists).
"""
from typing import List


def diff_list(nums: List) -> List:
    """
    Computes the diff list of nums which is a list composed of A[i] - A[i - 1] elements.

    >>> diff_array([1, 5, 3])
    >>> [0, 4, -2, 0]
    """
    n = len(nums)
    diff = [0] * (n + 1)  # 1 extra room for range increments
    diff[0] = nums[0]  # initialization

    for i in range(1, n):
        diff[i] = nums[i] - nums[i - 1]

    return diff


def range_update(diffs: List, left: int, right: int, value: int) -> None:
    diffs[left] += value
    diffs[right + 1] -= value


def apply_range_updates(nums: List, updated_diffs: List) -> None:
    """
    Applies all changes to the nums array (mutates it) based on the updated diffs list.
    """
    n = len(nums)

    for i in range(0, n):
        if i == 0:
            nums[0] = updated_diffs[0]
        else:
            nums[i] = updated_diffs[i] + nums[i - 1]
