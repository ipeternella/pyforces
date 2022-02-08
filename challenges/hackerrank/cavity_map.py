"""
Solution for: Cavity Map

https://www.hackerrank.com/challenges/cavity-map/problem
"""
import os
import sys

INF = sys.maxsize


def main():
    n = int(input())
    grid = [[] for _ in range(n)]

    for r in range(n):
        grid[r] = [int(digit) for digit in input().rstrip()]

    for r in range(1, n - 1):
        for c in range(1, n - 1):
            adjacent = [grid[r - 1][c], grid[r + 1][c], grid[r][c - 1], grid[r][c + 1]]
            is_deeper = [grid[r][c] > adj for adj in adjacent]

            if all(is_deeper):
                grid[r][c] = INF  # X

    for r in range(n):
        g = [str(ch) if ch != INF else "X" for ch in grid[r]]
        print("".join(g))


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
