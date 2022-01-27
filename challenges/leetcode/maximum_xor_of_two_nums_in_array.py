"""
Solution for LC#421: Maximum XOR of Two Numbers in an Array

https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
"""
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask, max_xor = 0, 0

        # max_xor will have up to 31 set bits for a 32-bit based int (excluding sign bit)
        for i in range(31, -1, -1):
            mask |= 1 << i  # mask to pick a range (1 to 31) of the most significant bits from the nums
            local_max = max_xor | (1 << i)  # gradually tries to pick more set bits that are possible in max_xor
            bit_prefixes = set()

            # filters only the most significant bits from the nums to see if these can lead to local_max's bits
            for num in nums:
                bit_prefixes.add(num & mask)

            for prefix in bit_prefixes:
                # another prefix allows this prefix to reach local_max: so there are two nums bits prefixes that
                # lead to local_max which means the ith bit can be achieved and is in the max_xor value,
                # so update max_xor!
                if prefix ^ local_max in bit_prefixes:
                    max_xor = local_max
                    break

        return max_xor
