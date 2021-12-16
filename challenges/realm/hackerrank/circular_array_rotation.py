"""
Solution for: Circular Array Rotation

https://www.hackerrank.com/challenges/circular-array-rotation/problem
"""
from typing import List


def circularArrayRotation(a: List[int], n: int, k: int, queries: List[int]) -> List[int]:
    rotated_a = a[(n - k % n) :] + a[0 : (n - k % n)]  # k % n to avoid k > n
    return [rotated_a[i] for i in queries]


if __name__ == "__main__":
    inputs = input().rstrip().split()
    n, k, q = int(inputs[0]), int(inputs[1]), int(inputs[2])
    a = list(map(int, input().rstrip().split()))
    queries = [int(input().strip()) for _ in range(q)]

    print("\n".join(map(str, circularArrayRotation(a, n, k, queries))))
