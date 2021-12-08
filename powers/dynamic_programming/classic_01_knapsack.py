"""
Classic (0-1) knapsack problem.
"""
import sys
from typing import List

INF = sys.maxsize


# O(2^N)
def knapsack_bruteforce(values: List[int], weights: List[int], max_weight: int) -> int:
    n = len(weights)

    def take(i: int, curr_weight: int) -> int:
        if i > n - 1:
            return 0

        # binary decision: take it or not
        take_it = 0
        if curr_weight + weights[i] <= max_weight:
            take_it = values[i] + take(i + 1, curr_weight + weights[i])

        dont_take_it = take(i + 1, curr_weight)
        return max(take_it, dont_take_it)

    return take(0, 0)


def knapsack_memoized(values: List[int], weights: List[int], max_weight: int) -> int:
    n = len(weights)
    state = [[-1] * (max_weight + 1) for _ in range(n)]  # state[n][max_weight + 1] or use a hashmap with tuples

    def take(i: int, curr_weight: int, state: List[List[int]]) -> int:
        # base case
        if i > n - 1:
            return 0

        # memo
        if state[i][curr_weight] != -1:
            return state[i][curr_weight]

        # problem solving with recursion
        take_it = 0
        if curr_weight + weights[i] <= max_weight:
            take_it = values[i] + take(i + 1, curr_weight + weights[i], state)

        dont_take_it = take(i + 1, curr_weight, state)
        state[i][curr_weight] = max(take_it, dont_take_it)

        return state[i][curr_weight]

    return take(0, 0, state)
