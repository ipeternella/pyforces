"""
Solution for Hackerrank: Text Wrap

 https://www.hackerrank.com/challenges/text-wrap/problem
"""
import os
import sys
from io import StringIO as StrBuilder


def main():
    s, w = input(), int(input())
    n = len(s)
    i = 0
    text = StrBuilder()

    while i < n:
        line = StrBuilder()

        for _ in range(w):
            if i > n - 1:
                break

            line.write(s[i])
            i += 1

        if line.getvalue():
            line.write("\n")
            text.write(line.getvalue())

    return text.getvalue()


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    print(main())
