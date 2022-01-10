"""
Solution for LC#191: Number of 1 Bits

https://leetcode.com/problems/number-of-1-bits/
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0

        while n:
            bits = bits + 1 if n & 1 == 1 else bits
            n >>= 1

        return bits
