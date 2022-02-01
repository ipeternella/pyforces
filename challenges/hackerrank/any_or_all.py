"""
Solution for Hackerrank: Any or All

https://www.hackerrank.com/challenges/any-or-all/problem
"""
import os
import sys


def is_palindrome(x: int) -> bool:
    s = str(x)
    l = 0
    r = len(s) - 1

    while l <= r:
        if s[l] != s[r]:
            return False

        l += 1
        r -= 1

    return True


def main():
    _ = int(input())
    nums = list(map(int, input().split()))
    if all(map(lambda x: x >= 0, nums)):
        print(any(map(is_palindrome, nums)))
    else:
        print(False)


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
