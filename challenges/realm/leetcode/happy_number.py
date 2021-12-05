"""
Solution for LC#202: Happy Number

https://leetcode.com/problems/happy-number/
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def happy_split(n: int) -> int:
            new_n = 0

            while n > 0:
                digit = n % 10
                n //= 10
                new_n += digit ** 2

            return new_n

        # Floyd's cyclic detection algorithm: tortoise runner (slow) and hare runner (fast)
        slow = n
        fast = happy_split(n)  # starts 1 position ahead

        while fast > 1:
            slow = happy_split(slow)  # 1x runner
            fast = happy_split(happy_split(fast))  # 2x runner

            if fast == slow:  # cycle detection
                return False

        return True


class SolutionHashSet:
    def isHappy(self, n: int) -> bool:
        def happy_split(n: int) -> int:
            new_n = 0

            while n > 0:
                digit = n % 10
                n //= 10
                new_n += digit ** 2

            return new_n

        prev_splits = set()  # cycle-detection with hashset
        while n > 1:
            prev_splits.add(n)
            n = happy_split(n)

            if n in prev_splits:
                return False

        return True
