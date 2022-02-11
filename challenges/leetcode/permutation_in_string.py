"""
Solution for LC#567: Permutation in String

https://leetcode.com/problems/permutation-in-string/
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        s1_chars = Counter(s1)
        s2_window = Counter(s2[0:n])  # first window

        if s1_chars == s2_window:
            return True

        for i in range(1, m - n + 1):
            # sliding window update
            old_ch = s2[i - 1]
            new_ch = s2[i + n - 1]

            s2_window[new_ch] += 1
            s2_window[old_ch] -= 1

            if s2_window[old_ch] <= 0:
                s2_window.pop(old_ch)

            # check if chars frequency match == anagram!
            if s1_chars == s2_window:
                return True

        return False
