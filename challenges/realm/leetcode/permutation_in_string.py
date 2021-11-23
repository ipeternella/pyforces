"""
Solution for LC#567: Permutation in String

https://leetcode.com/problems/permutation-in-string/
"""
from typing import Dict


def add_freq(key: str, d: Dict, required: Dict):
    if key in required:
        if key in d:
            d[key] += 1
        else:
            d[key] = 1


def remove_freq(key: str, d: Dict, required: Dict):
    if key in required:
        d[key] -= 1


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        required: Dict[str, int] = dict()
        freqs: Dict[str, int] = dict()

        if n > m:
            return False  # pattern > str: impossible

        # parses s1 to get freq. distribution of the pattern
        for ch in s1:
            required[ch] = 1 if ch not in required else required[ch] + 1

        # first window - [0, n)
        for i in range(0, n):
            ch = s2[i]
            add_freq(ch, freqs, required)

        if freqs == required:
            return True

        for i in range(n, m):
            # sliding windows - [n, m)
            ch_out = s2[i - n]
            ch_in = s2[i]

            remove_freq(ch_out, freqs, required)  # out of the window: remove freq
            add_freq(ch_in, freqs, required)  # in the window: add freq

            if required == freqs:
                return True

        return False
