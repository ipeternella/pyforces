"""
Solution for LC#67: Add Binary

https://leetcode.com/problems/add-binary/
"""
from io import StringIO


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int, b_int = 0, 0
        buffer = StringIO()

        # form integers from their individual bits
        for bit in a:
            a_int <<= 1
            a_int |= int(bit)

        for bit in b:
            b_int <<= 1
            b_int |= int(bit)

        # sum ints and extract each individual bit
        # if c == 0, return "0" as the while loop won't run
        c = a_int + b_int

        while c:
            buffer.write(str(c & 1))
            c >>= 1

        rslt = buffer.getvalue()[::-1]
        return rslt if rslt else "0"
