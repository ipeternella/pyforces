"""
Solution for: Equal Stacks

https://www.hackerrank.com/challenges/equal-stacks/problem
"""
from typing import List


def equalStacks(h1: List[int], h2: List[int], h3: List[int]) -> int:
    n1, n2, n3 = len(h1), len(h2), len(h3)
    s1, s2, s3 = sum(h1), sum(h2), sum(h3)
    i1, i2, i3 = 0, 0, 0

    while s1 != s2 or s1 != s3 or s2 != s3:
        if s1 >= s2 and s1 >= s3:
            s1 -= h1[i1]
            i1 += 1
        elif s2 >= s1 and s2 >= s3:
            s2 -= h2[i2]
            i2 += 1
        elif s3 >= s1 and s3 >= s2:
            s3 -= h3[i3]
            i3 += 1

        if i1 > n1 - 1 or i2 > n2 - 1 or i3 > n3 - 1:
            return 0

    return s1


if __name__ == "__main__":
    n1, n2, n3 = list(map(int, input().rstrip().split()))
    h1 = list(map(int, input().rstrip().split())) if n1 > 0 else []
    h2 = list(map(int, input().rstrip().split())) if n2 > 0 else []
    h3 = list(map(int, input().rstrip().split())) if n3 > 0 else []

    print(equalStacks(h1, h2, h3))
