"""
Solution for LC#8: String to Integer (atoi)

https://leetcode.com/problems/string-to-integer-atoi/
"""
from io import StringIO

DIGITS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
MAX_INT = 2 ** 31 - 1
MIN_INT = -(2 ** 31)


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        buffer = StringIO()
        must_be_digit = False
        positive = True

        for i in range(len(s)):
            ch = s[i]

            if ch not in DIGITS:
                if must_be_digit:  # after a '+', '-', digit: only digits will be allowed
                    break

                if ch == "-":
                    positive = False
                    must_be_digit = True
                elif ch == "+":
                    positive = True
                    must_be_digit = True
                else:
                    break  # against 'z2'
            else:
                must_be_digit = True  # against unknown symbols in the middle of digits '22+2' -> 22
                buffer.write(ch)

        num_s = buffer.getvalue()
        if not num_s:  # empty buffer
            return 0

        # final clamping: Python handles big ints, so it's easier here
        num = int(num_s)
        if positive:
            return num if num <= MAX_INT else MAX_INT

        return -num if -num >= MIN_INT else MIN_INT
