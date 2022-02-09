"""
Solution for LC#525: Contiguous Array 

https://leetcode.com/problems/contiguous-array/
"""
import sys
from typing import List

INF = sys.maxsize


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        offset = 0  # offset from balanced state in which number of 0s == number of 1s
        balances = dict()

        # capture list of offsets for each number (offset from state in which 0s and 1s are balanced)
        for i in range(n):
            offset = offset - 1 if nums[i] == 0 else offset + 1

            if offset not in balances:
                balances[offset] = [i]
            else:
                balances[offset].append(i)

        max_dist = 0
        for offset, dists in balances.items():
            m = len(dists)

            if offset == 0:
                # offset == 0 means a subarray with balanced number of 1s and 0s starting from i == 0
                max_dist = max(max_dist, dists[m - 1] + 1)  # grab furthest index @ m - 1
            elif offset != 0 and m > 1:
                # dists[m - 1] - dists[0] == longest subarray that corrects unbalanced 1s or 0s
                max_dist = max(max_dist, dists[m - 1] - dists[0])  # grab the biggest diff in indexes

        return max_dist
