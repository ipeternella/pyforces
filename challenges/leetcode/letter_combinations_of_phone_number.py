"""
Solution for LC#17: Letter Combinations of a Phone Number

https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def combine_backtrack(comb, i):
            if n < 1:
                return

            if i > n - 1:
                combinations.append("".join(comb))
                return

            letters = digit_letters[i]
            for j in range(len(letters)):
                comb.append(letters[j])
                combine_backtrack(comb, i + 1)
                comb.pop()

        n = len(digits)
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        digit_letters = [mapping[int(digit)] for digit in digits]
        combinations: List[str] = []

        combine_backtrack([], 0)
        return combinations
