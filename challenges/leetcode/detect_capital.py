"""
Solution for LC#520: Detect Capital

https://leetcode.com/problems/detect-capital/
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        is_first_upper = word[0].isupper()

        if len(word) == 1:
            return True
        elif is_first_upper:
            return word[1:].isupper() or word[1:].islower()

        return word[1:].islower()
