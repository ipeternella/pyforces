"""
Solution for Hackerrank: Calendar Module 

https://www.hackerrank.com/challenges/calendar-module/problem
"""
import os
import sys
from datetime import datetime

if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    raw_dt = input().rstrip()
    dt = datetime.strptime(raw_dt, "%m %d %Y").date()

    print(dt.strftime("%A").upper())
