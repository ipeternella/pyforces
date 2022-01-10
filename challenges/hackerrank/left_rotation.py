"""
Solution for: Left Rotation

https://www.hackerrank.com/challenges/array-left-rotation/problem
"""
from typing import List


def rotateLeft(d: int, arr: List[int]) -> List[int]:
    return arr[d:] + arr[0:d]


if __name__ == "__main__":
    d = int(input().rstrip().split()[1])
    arr = list(map(int, input().rstrip().split()))

    print(" ".join(map(str, arr[d:] + arr[0:d])))
