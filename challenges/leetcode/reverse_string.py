"""
Solution for 344. Reverse String.

https://leetcode.com/problems/reverse-string/
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def swap(i: int, j: int) -> None:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp

        start = 0
        end = len(s) - 1

        while start <= end:
            swap(start, end)
            start += 1
            end -= 1
