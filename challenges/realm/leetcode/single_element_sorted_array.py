"""
Solution for LeetCode: Single Element in a Sorted Array (LC#540).

https://leetcode.com/problems/single-element-in-a-sorted-array/
"""

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def compare(prev, mid, nxt):
            if prev != -1 and a[mid] == a[prev]:
                return -1

            if nxt != -1 and a[mid] == a[nxt]:
                return 1

            return 0  # found

        a = nums
        n = len(a)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            nxt = mid + 1 if mid < n - 1 else -1
            prev = mid - 1 if mid > 0 else -1
            check = compare(prev, mid, nxt)

            # binary searching according to the length of the left/right arrays
            if check == 0:
                return a[mid]  # found it!
            elif check < 0:
                left_n = mid - left + 1

                if left_n % 2 != 0:
                    right = mid - 2  # single element is on the left
                else:
                    left = mid + 1  # single element is on the right
            else:
                left_n = mid - left

                if left_n % 2 != 0:
                    right = mid - 1
                else:
                    left = mid + 2

        return nums[0]
