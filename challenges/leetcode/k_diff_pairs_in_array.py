"""
Solution for LC#532: K-diff Pairs in an Array 

https://leetcode.com/problems/k-diff-pairs-in-an-array/
"""
import sys
from typing import List

INF = sys.maxsize


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        def has_target(arr, l, r, target):  # binary search
            while l <= r:
                mid = (l + r) // 2

                if arr[mid] < target:
                    l = mid + 1
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    return True

            return False

        n = len(nums)
        nums = sorted(nums)
        prev = INF
        pairs = 0

        for i in range(n - 1):
            curr = nums[i]
            if prev != INF and prev == curr:
                continue

            target = k + curr
            if has_target(nums, i + 1, n - 1, target):
                pairs += 1

            prev = curr

        return pairs
