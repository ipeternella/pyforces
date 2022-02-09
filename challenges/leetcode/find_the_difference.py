"""
Solution for LC#389: Find the Difference

https://leetcode.com/problems/find-the-difference/
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_letters, t_letters = dict(), dict()
        added_ch = ""

        for ch in s:
            s_letters[ch] = s_letters.get(ch, 0) + 1

        for ch in t:
            t_letters[ch] = t_letters.get(ch, 0) + 1

        for ch, freq in t_letters.items():
            if s_letters.get(ch, 0) != freq:
                added_ch = ch
                break

        return added_ch
