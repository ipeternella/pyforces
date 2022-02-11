"""
Solution for LC#560: Subarray Sum Equals K 

https://leetcode.com/problems/subarray-sum-equals-k/
"""
from typing import List


# O(N) solution
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


# O(N^2) solution, but TLEs in Python
class SolutionPrefixSums:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        prefix_sums = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

        for l in range(n):
            for r in range(l, n):
                # for range sum [l, r] of nums we must use [l, r + 1] on prefix_sums
                range_sum = prefix_sums[r + 1] - prefix_sums[l]
                if range_sum == k:
                    total += 1

        return total
