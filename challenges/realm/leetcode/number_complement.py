"""
Solution for LC#476: Number Complement

https://leetcode.com/problems/number-complement/
"""


class Solution:
    def findComplement(self, num: int) -> int:
        bits = 0
        num_copy = num

        # bit counting
        while num_copy:
            bits += 1
            num_copy >>= 1

        # mask to remove left-most bits (including sign bit)
        mask = ~(~0 << bits)
        return ~num & mask
