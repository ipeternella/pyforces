"""
Solution for LC#168: Excel Sheet Column Title

https://leetcode.com/problems/excel-sheet-column-title/
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ref = 0
        p = 0

        # ref for A-based columns follows: ... + 26^2 + 26^1 + 26^0
        while ref <= columnNumber:
            ref += 26**p
            p += 1

        # remove extra addition of previous loop to discover ref and number of letters
        ref -= 26 ** (p - 1)  # number form columns based on "A" like "AA", "AAA", etc.
        n = p - 1

        # work with the remaining from "A", or "AA", "AAA", etc.
        remaining = columnNumber - ref
        column_title = ["A"] * n

        p = n - 1
        for i in range(n):
            offset = remaining // (26**p)  # if offset == 0: no changes to column_title[i]
            column_title[i] = chr((offset + ord("A")))

            remaining -= offset * (26**p)
            p -= 1

        return "".join(column_title)
