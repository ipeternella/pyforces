"""
Solution for LC#9: Palindrome Number

https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = x
        x_reverse = 0

        while tmp > 0:
            x_reverse = x_reverse * 10 + tmp % 10
            tmp //= 10

        return x_reverse == x  # palindromic number: reversed digits should be the same number
