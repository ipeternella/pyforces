"""
Solution for: 3D Surface Area

https://www.hackerrank.com/challenges/3d-surface-area/problem
"""
import os
import sys


def main():
    h, w = map(int, input().rstrip().split())
    board = [[] for _ in range(h)]

    for i in range(h):
        board[i] = list(map(int, input().rstrip().split()))

    row_area = 0
    for r in range(h):
        for c in range(w + 1):
            h1 = board[r][c - 1] if c - 1 >= 0 else 0
            h2 = board[r][c] if c < w else 0

            row_area += abs(h1 - h2)

    column_area = 0
    for c in range(w):
        for r in range(h + 1):
            h1 = board[r - 1][c] if r - 1 >= 0 else 0
            h2 = board[r][c] if r < h else 0

            column_area += abs(h1 - h2)

    top_area = h * w
    bottom_area = h * w

    print(row_area + column_area + top_area + bottom_area)


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
