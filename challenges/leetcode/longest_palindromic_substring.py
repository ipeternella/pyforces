"""
Solution for LC#5: Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_size = 0
        longest = ""
        n = len(s)

        # concentric palindromes approach: a bigger palindrome can be detected in O(1) if
        # the first and last chars are the same so we can get an overall algorithm with O(N^2)
        # time complexity and O(1) space complexity
        for center in range(n):
            i, j = center, center

            # odd palindromes
            while i >= 0 and j <= n - 1:
                substr = s[i : j + 1]
                m = len(substr)

                if substr[0] == substr[m - 1]:  # always start as a palindrome (1 char substring)
                    if m > longest_size:
                        longest = substr
                        longest_size = m
                else:
                    break  # impossible to be a palindrome: symmetry around center was broken

                i -= 1
                j += 1

            # even palindromes (center is "imaginary" between two chars)
            i, j = center - 1, center
            while i >= 0 and j <= n - 1:
                substr = s[i : j + 1]
                m = len(substr)

                if substr[0] == substr[m - 1]:
                    if m > longest_size:
                        longest = substr
                        longest_size = m
                else:
                    break  # impossible to be a palindrome: symmetry around center was broken

                i -= 1
                j += 1

        return longest
