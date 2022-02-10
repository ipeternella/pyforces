"""
Solution for LC#560: Subarray Sum Equals K 

https://leetcode.com/problems/subarray-sum-equals-k/
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        sum_freqs = {0: 1}  # { sum: freq } starts with sum zero
        s = 0
        for i in range(n):
            # if current sum == s, if we have a previous (s - k) in the sum_freqs
            # it means between (s - k) .. s a subarray of sum k occured
            s += nums[i]
            total += sum_freqs.get(s - k, 0)
            sum_freqs[s] = sum_freqs.get(s, 0) + 1

        return total
