"""
Solution for LC#70: Climbing Stairs

https://leetcode.com/problems/climbing-stairs/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        ways = [0] * (n)  # state
        ways[0] = 1
        ways[1] = 1

        for step in range(1, n):
            for jump in (1, 2):
                if step - jump >= 0:
                    ways[step] += ways[step - jump]

        return ways[n - 1]
