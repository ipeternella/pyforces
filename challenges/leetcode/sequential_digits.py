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

        def seq_num(digit, total_digits):
            base = 10 ** (total_digits - 1)
            count = 0
            num = 0

            while count != total_digits:
                if digit > 9:
                    return num, True

                num += base * digit
                base //= 10
                digit += 1
                count += 1

            return num, False

        nums: List[int] = []
        for total_digits in range(count_digits(low), count_digits(high) + 1):
            for first_digit in range(1, 10):
                num, excess = seq_num(first_digit, total_digits)

                if excess:
                    continue

                if low <= num <= high:
                    nums.append(num)

        return nums
