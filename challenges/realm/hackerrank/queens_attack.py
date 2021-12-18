"""
Solution for: Queen's Attack II

https://www.hackerrank.com/challenges/queens-attack-2/problem
"""
from typing import Set
from typing import Tuple


def queensAttack(n: int, k: int, r_q: int, c_q: int, obstacles: Set[Tuple[int, int]]) -> int:
    moves = 0

    # right
    for c in range(c_q + 1, n):
        if (r_q, c) in obstacles:
            break
        moves += 1

    # left
    for c in range(c_q - 1, -1, -1):
        if (r_q, c) in obstacles:
            break
        moves += 1

    # up
    for r in range(r_q - 1, -1, -1):
        if (r, c_q) in obstacles:
            break
        moves += 1

    # down
    for r in range(r_q + 1, n):
        if (r, c_q) in obstacles:
            break
        moves += 1

    # main diag (upper left)
    r, c = r_q - 1, c_q - 1
    while r >= 0 and c >= 0:
        if (r, c) in obstacles:
            break
        r, c = r - 1, c - 1
        moves += 1

    # main diag (bottom right)
    r, c = r_q + 1, c_q + 1
    while r < n and c < n:
        if (r, c) in obstacles:
            break
        r, c = r + 1, c + 1
        moves += 1

    # other diag (upper right)
    r, c = r_q - 1, c_q + 1
    while r >= 0 and c < n:
        if (r, c) in obstacles:
            break
        r, c = r - 1, c + 1
        moves += 1

    # other diag (bottom left)
    r, c = r_q + 1, c_q - 1
    while r < n and c >= 0:
        if (r, c) in obstacles:
            break
        r, c = r + 1, c - 1
        moves += 1

    return moves


if __name__ == "__main__":
    inputs = input().rstrip().split()
    n, k = int(inputs[0]), int(inputs[1])

    inputs = input().rstrip().split()
    r_q, c_q = (n - 1) - (int(inputs[0]) - 1), int(inputs[1]) - 1  # translation to (0, 0)

    obstacles = set()
    for _ in range(k):
        r_i, c_i = list(map(int, input().rstrip().split()))
        obstacles.add(((n - 1) - (r_i - 1), c_i - 1))  # translation to (0, 0)

    print(queensAttack(n, k, r_q, c_q, obstacles))
