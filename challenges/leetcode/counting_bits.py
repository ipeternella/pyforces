"""
Solution for LC#338: Counting Bits

https://leetcode.com/problems/counting-bits/
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        pow2_next = 1

        for i in range(1, n + 1):
            num = i

            if num == pow2_next:
                dp[num] = 1  # power of 2: always one bit is required (e.g.: 8 -> 1000, 4 -> 0100, 2 -> 0010, etc.)
                pow2_next *= 2
            else:
                # decompose binary num into: num = pow2 + x where x < pow2
                # solve for x to decompose the num as: pow2 + (num - pow2)
                # and use dynammic programming to fetch previous states
                pow2 = pow2_next // 2  # pow2_next is always ahead by x2, so divide it!
                dp[num] = dp[pow2] + dp[num - pow2]

        return dp
