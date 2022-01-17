"""
Solution for LC#290: Word Pattern

https://leetcode.com/problems/word-pattern/
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        matches = dict()
        words = s.split()
        n = len(pattern)
        i = 0

        # against cases in which pattern has fewer or more symbols than required by words
        if len(pattern) != len(words) or (len(set(pattern)) != len(set(words))):
            return False

        for word in words:
            if i > n - 1:
                return False

            p = pattern[i]
            if p not in matches:
                matches[p] = word
            elif matches[p] != word:
                return False

            i += 1

        return i == n
