"""
Solution for LC#1291: Sequential Digits

https://leetcode.com/problems/sequential-digits/
"""
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def count_digits(num):
            digits = 0
            while num != 0:
                num //= 10
                digits += 1

            return digits

        def create_seq_nums(total_digits):
            # for a total_digits like 3 it builds: 100 + 20 + 3, 200 + 30 + 4, ...
            for digit in range(1, 10):
                base = 10 ** (total_digits - 1)
                num = 0
                amount_digits = 0

                while amount_digits != total_digits:
                    if digit > 9:
                        return

                    num += base * digit
                    base //= 10
                    digit += 1
                    amount_digits += 1

                if low <= num <= high:
                    nums.append(num)

        low_digits = count_digits(low)
        high_digits = count_digits(high)
        nums: List[int] = []

        for digits in range(low_digits, high_digits + 1):
            create_seq_nums(digits)

        return nums
