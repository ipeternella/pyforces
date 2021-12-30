"""
Solution for LC#461: Hamming Distance

https://leetcode.com/problems/hamming-distance/
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        hamming = 0

        while diff:
            hamming = hamming + 1 if diff & 1 == 1 else hamming
            diff >>= 1

        return hamming
