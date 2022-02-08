"""
Solution for: The Bomberman Game

https://www.hackerrank.com/challenges/bomber-man/problem
"""
import os
import sys


def fill_and_explode(grid, r, c, times=1):
    for _ in range(times):

        for i in range(r):
            for j in range(c):
                grid[i][j] = "O" if grid[i][j] == "." else "X"

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "X":
                    grid[i][j] = "."
                    adjacent = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

                    for adj_i, adj_j in adjacent:
                        if 0 <= adj_i < r and 0 <= adj_j < c and grid[adj_i][adj_j] != "X":
                            grid[adj_i][adj_j] = "."


def print_grid(grid, r, c, is_full=False):
    if not is_full:
        for i in range(r):
            print("".join(grid[i]))
        return

    for i in range(r):
        print("O" * c)


def main():
    r, c, t = map(int, input().rstrip().split())
    grid = [[] for _ in range(r)]

    for i in range(r):
        grid[i] = [ch for ch in input().rstrip()]

    if t <= 1:
        print_grid(grid, r, c)
    elif t == 2:
        print_grid(grid, r, c, is_full=True)
    else:
        t = (t - 3) % 4  # from here on: the grid always repeats forever

        if t == 0:
            fill_and_explode(grid, r, c)
            print_grid(grid, r, c)
        elif t == 1 or t == 3:
            print_grid(grid, r, c, is_full=True)
        else:
            fill_and_explode(grid, r, c, times=2)
            print_grid(grid, r, c)


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
