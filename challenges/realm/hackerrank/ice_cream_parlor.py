"""
Solution for: Ice Cream Parlor

https://www.hackerrank.com/challenges/icecream-parlor/problem
"""
from typing import Dict
from typing import List


def icecreamParlor(target: int, costs: List[int]) -> List[int]:
    required: Dict[int, int] = dict()

    for i, cost in enumerate(costs):
        if cost in required:
            return sorted([i + 1, required[cost] + 1])

        required[target - cost] = i

    return []


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        target = int(input().strip())
        _ = int(input().strip())
        costs = list(map(int, input().rstrip().split()))

        print(" ".join(map(str, icecreamParlor(target, costs))))
