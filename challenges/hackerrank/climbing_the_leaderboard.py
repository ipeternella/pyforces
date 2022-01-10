"""
Solution for: Climbing The Leaderboard

https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""
import os
from typing import List


def reverse_binary_search(arr: List[int], score: int) -> int:
    n = len(arr)
    l = 0
    r = n - 1

    while l <= r:
        mid = (l + r) // 2

        if score > arr[mid]:
            r = mid - 1
        elif score < arr[mid]:
            l = mid + 1
        else:
            return mid

    if arr[mid] > score:
        return mid + 1

    return mid


def remove_duplicates(arr: List[int]) -> List[int]:
    new_arr = []
    used = set()

    for i, n in enumerate(arr):
        if n not in used:
            new_arr.append(n)
            used.add(n)

    return new_arr


def climbingLeaderboard(ranked: List[int], player: List[int]) -> List[int]:
    ranked = remove_duplicates(ranked)
    new_ranks = []

    for score in player:
        new_rank = reverse_binary_search(ranked, score)
        new_ranks.append(new_rank + 1)

    return new_ranks


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
