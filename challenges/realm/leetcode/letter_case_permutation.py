"""
Solution for LC#784: Letter Case Permutation

https://leetcode.com/problems/letter-case-permutation/
"""
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(i: int, chars: List[str]) -> None:
            if i > n - 1:
                permutations.append("".join(chars))
                return

            ch = s[i]
            if not ch.isdigit():
                chars.append(ch.upper())
                backtrack(i + 1, chars)
                chars.pop()

                chars.append(ch.lower())
                backtrack(i + 1, chars)
                chars.pop()
            else:
                chars.append(ch)
                backtrack(i + 1, chars)
                chars.pop()

        n = len(s)
        permutations: List[str] = []

        backtrack(0, [])
        return permutations
