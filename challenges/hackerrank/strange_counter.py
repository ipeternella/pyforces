"""
Solution for: Strange Counter

https://www.hackerrank.com/challenges/strange-code/problem
"""
import os
import sys


def main():
    t = int(input())
    t_guess = 1
    t_base = t_guess

    while t_guess <= t:
        t_base = t_guess
        t_guess = 2 * t_guess + 2

    value = t_base + 2
    diff = t - t_base

    print(value - diff)


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
