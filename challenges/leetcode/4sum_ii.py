"""
Solution for LC#454: 4Sum II

https://leetcode.com/problems/4sum-ii/
"""
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        sum_freqs = dict()
        total = 0

        # for the given problem it must be true that: (n3 + n4) == -(n1 + n2)
        # hence we pre-compute/cache all the possible sums of n3 + n4 in a hashmap
        # to avoid repeated and unnecessary computations and get a O(N^2) running time so
        # we trade O(N^4) time complexity for O(N^2) time + O(N^2) space complexity
        for i in range(n):
            for j in range(n):
                s = nums3[i] + nums4[j]
                sum_freqs[s] = sum_freqs.get(s, 0) + 1

        for n1 in nums1:
            for n2 in nums2:
                partial_target = -(n1 + n2)
                total += sum_freqs.get(partial_target, 0)

        return total
