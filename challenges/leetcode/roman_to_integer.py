"""
Solution for LC#13: Roman to Integer

https://leetcode.com/problems/roman-to-integer/
"""
mapping = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "CD": 400,
    "CM": 900,
    "XL": 40,
    "XC": 90,
    "IV": 4,
    "IX": 9,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i = 0
        n = len(s)

        while i < n:
            ch = s[i]
            two_chs = f"{s[i]}{s[i + 1]}" if i < n - 1 else ""

            if two_chs in mapping:
                num += mapping[two_chs]
                i += 2
            else:
                num += mapping[ch]
                i += 1

        return num
