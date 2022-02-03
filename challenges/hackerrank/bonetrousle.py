"""
Solution for: Bonetrousle

https://www.hackerrank.com/challenges/bonetrousle/problem
"""
import os
import sys


def main():
    t = int(input())

    for _ in range(t):
        n, k, b = map(int, input().split())

        # basic manipulation of arithmetic progression's sum formula for AP of: [1 .. k] elements
        min_sticks = b * (b + 1) // 2  # min sticks: AP sum of the left-most range: [1 .. b]
        max_sticks = b * (2 * k - b + 1) // 2  # max sticks: AP sum of the right-most range: [k - b + 1 .. k]

        # impossible: for b boxes, target n is below or beyond the arithmetic progression given by 1 .. k
        if n < min_sticks or n > max_sticks:
            print(-1)
            continue

        # start with the left-most (min_sticks sum)
        boxes = [i for i in range(1, b + 1)]

        # add what's missing from the target n (n - min_sticks) but divide it evenly
        # among the b sticks that we have in the boxes variable
        missing = (n - min_sticks) // b
        missing_r = (n - min_sticks) % b

        for i in range(b):
            boxes[i] += missing

        j = b - 1
        for _ in range(missing_r):
            boxes[j] += 1
            j -= 1

        print(" ".join(map(str, boxes)))


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
