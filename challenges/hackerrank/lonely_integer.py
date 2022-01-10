"""
Solution for: Lonely Integer

https://www.hackerrank.com/challenges/lonely-integer/problem
"""
from typing import List


def lonelyinteger(a: List[int]) -> int:
    mask = 0
    for num in a:
        mask ^= num

    return mask


if __name__ == "__main__":
    _ = input()
    a = list(map(int, input().rstrip().split()))

    print(lonelyinteger(a))
