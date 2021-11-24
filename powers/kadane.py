"""
Kadane's algorithm for finding the largest sum of subarrays in O(N).
"""
from typing import List


def kadane(nums: List[int]) -> int:
    """
    DP and greedy algorithm: Greedy as starting a new range is better
    than starting with a more negative sum.
    """
    n = len(nums)
    global_max = nums[0]
    prev_local_max = nums[0]

    for i in range(1, n):
        # starts new range when previous local max is worse (<) than nums[i]
        prev_local_max = max(nums[i], nums[i] + prev_local_max)
        global_max = max(global_max, prev_local_max)

    return global_max
