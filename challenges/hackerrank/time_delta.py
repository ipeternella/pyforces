"""
Solution for Hackerrank: Time Delta

https://www.hackerrank.com/challenges/python-time-delta/problem
"""
import os
import sys
from datetime import datetime


def main():
    t = int(input())
    for _ in range(t):
        t1 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
        t2 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
        print(int(abs(t2.timestamp() - t1.timestamp())))


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
