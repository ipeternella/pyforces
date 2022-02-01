"""
Solution for Hackerrank: No Idea!

https://www.hackerrank.com/challenges/no-idea/problem
"""
import os
import sys


def main():
    input()
    nums = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    h = 0

    for num in nums:
        if num in a:
            h += 1
        if num in b:
            h -= 1

    print(h)


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
