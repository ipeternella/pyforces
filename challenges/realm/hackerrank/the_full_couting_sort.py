"""
Solution for: The Full Counting Sort

https://www.hackerrank.com/challenges/countingsort4/problem
"""
from typing import List


def countSort(arr: List[List[str]]) -> None:
    n = len(arr)
    freqs = [0] * 100
    mapping: List[List[str]] = [[] for _ in range(100)]

    for i, tpl in enumerate(arr):
        x = int(tpl[0])
        s = "-" if i < n // 2 else tpl[1]
        freqs[x] += 1
        mapping[x].append(s)

    for i, freq in enumerate(freqs):
        j = freq
        while freq > 0:
            print(mapping[i][j - freq], end=" ")
            freq -= 1


if __name__ == "__main__":
    n = int(input().strip())
    arr = [input().rstrip().split() for _ in range(n)]

    countSort(arr)
