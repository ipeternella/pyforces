"""
Solution for LC#402: Remove K Digits

https://leetcode.com/problems/remove-k-digits/
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k >= n:
            return "0"

        # monotonically increasing stack to leave smaller
        # digits to the left as much as possible
        mono_stack = []
        for ch in num:
            digit = int(ch)

            if not mono_stack:
                mono_stack.append(digit)
            else:
                while k > 0 and mono_stack and digit < mono_stack[-1]:
                    mono_stack.pop()
                    k -= 1

                mono_stack.append(digit)

        # remaining K (it may still be necessary to trim some digits) but as
        # the numbers increase monotonically now we can trim right-most nums
        for _ in range(k):
            mono_stack.pop()  # trim right-most nums

        # build final number
        number = "".join(map(str, mono_stack))
        return str(int(number))
