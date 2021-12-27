"""
Solution for LC#190: Reverse Bits

https://leetcode.com/problems/reverse-bits/
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        set_bits = n.bit_length()

        while n:
            reverse <<= 1
            bit = n & 1  # reads each bit
            reverse |= bit  # inserts the bit and shifts left on next iter
            n >>= 1

        return reverse << (32 - set_bits)
