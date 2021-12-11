"""
Solution for: The Coin Change Problem

https://www.hackerrank.com/challenges/coin-change/problem
"""
from typing import Dict
from typing import List
from typing import Tuple


def getWays(n: int, c: List[int]) -> int:
    def dp(remaining: int, i: int, state: Dict[Tuple[int, int], int]):
        if remaining < 0:
            return 0

        if remaining == 0:
            return 1

        if (remaining, i) in state:
            return state[(remaining, i)]

        ways = 0
        for j in range(i, m):
            coin = c[j]
            ways += dp(remaining - coin, j, state)

        state[(remaining, i)] = ways
        return state[(remaining, i)]

    m = len(c)
    return dp(n, 0, dict())  # hashmap of 2-tuples or 2D matrix for memoization


if __name__ == "__main__":
    n = int(input().rstrip().split()[0])
    coins = list(map(int, input().rstrip().split()))

    print(getWays(n, coins))
