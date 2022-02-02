"""
Solution for LC#438: Find All Anagrams in a String

https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        freq_p = Counter(p)
        ans = []

        # sliding window: first window
        window_freq = Counter(s[0:n])
        if window_freq == freq_p:
            ans.append(0)

        for i in range(1, m - n + 1):
            new_ch = s[i + n - 1]  # abcd
            old_ch = s[i - 1]

            # window updating
            window_freq[new_ch] = window_freq.get(new_ch, 0) + 1
            window_freq[old_ch] -= 1

            if window_freq[old_ch] <= 0:
                window_freq.pop(old_ch)

            if window_freq == freq_p:
                ans.append(i)

        return ans
