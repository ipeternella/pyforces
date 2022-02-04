"""
Solution for: Maximum Sum

https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/maximum-sum-4-f8d12458/
"""
import os
import sys


def main():
    _ = int(input())
    nums = list(map(int, input().split()))
    positives = [num for num in nums if num >= 0]

    if len(positives) == 0:  # no pos numbers
        print(max(nums), 1)
    else:
        print(sum(positives), len(positives))


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
