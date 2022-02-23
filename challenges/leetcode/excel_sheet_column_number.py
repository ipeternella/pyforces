"""
Solution for LC#171: Excel Sheet Column Number

https://leetcode.com/problems/excel-sheet-column-number/
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        p = n - 1
        i = 0
        column_number = 0

        while p >= 0 and i < n:
            column_number += (ord(columnTitle[i]) - ord("A") + 1) * (26**p)
            i += 1
            p -= 1

        return column_number
