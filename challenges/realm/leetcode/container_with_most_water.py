"""
Solution for LC#11: Container With Most Water

https://leetcode.com/problems/container-with-most-water/
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        max_area = (r - l) * min(height[l], height[r])

        while l <= r:
            if height[l] < height[r]:
                l += 1
                max_area = max(max_area, (r - l) * min(height[l], height[r]))
            else:
                r -= 1
                max_area = max(max_area, (r - l) * min(height[l], height[r]))

        return max_area
