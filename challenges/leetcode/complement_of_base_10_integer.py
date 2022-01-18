"""
Solution for LC#1009: Complement of Base 10 Integer

https://leetcode.com/problems/complement-of-base-10-integer/
"""


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        m = n
        mask = 0 if n > 0 else 1

        while m:
            m >>= 1
            mask <<= 1
            mask |= 1

        return n ^ mask
