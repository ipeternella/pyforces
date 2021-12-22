"""
Solution for: Count Triplets

https://www.hackerrank.com/challenges/count-triplets-1/problem
"""
from collections import Counter
from typing import Dict
from typing import List


def countTriplets(arr: List[int], r: int) -> int:
    n = len(arr)
    nums_ahead = Counter(arr)
    nums_behind: Dict[int, int] = dict()
    triplets = 0

    # interpret each num as the middle one of the triplets (a, _b_, c)
    # requires a = b//r and c = a * r triplets
    for i in range(n - 1, -1, -1):
        b = arr[i]
        a = b // r
        c = b * r
        nums_ahead[b] -= 1  # we are at b

        # b must be multiple of r and must have a ahead and c behind
        if b % r == 0 and nums_ahead.get(a, 0) > 0 and nums_behind.get(c, 0) > 0:
            freq_a = nums_ahead[a]
            freq_c = nums_behind[c]
            triplets += freq_a * freq_c

        nums_behind[b] = nums_behind.get(b, 0) + 1  # b now goes behind

    return triplets


if __name__ == "__main__":
    nr = input().rstrip().split()
    n, r = int(nr[0]), int(nr[1])
    arr = list(map(int, input().rstrip().split()))

    print(countTriplets(arr, r))
