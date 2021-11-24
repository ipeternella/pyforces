"""
Module with an example of the sliding window technique which runs ins O(N) for arrays.
"""

from typing import List


def max_sum_k(nums: List[int], k: int) -> int:
    """
    Computes the max sum of the subarrays of size k.
    """
    n = len(nums)
    s = 0

    if k > n:
        return ValueError("k must be <= n!")

    # first window -> [0, k)
    s = sum(nums[:k])

    # sliding windows -> [k, n)
    for i in range(k, n):
        s -= nums[i - k]  # out of the window
        s += nums[i]  # inside the window

    return s
