"""
Solution for: Forming a Magic Square

https://www.hackerrank.com/challenges/magic-square-forming/problem
"""
import os
import sys


def main():
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    # 3x3 trivial variations from problem's wikipedia ref
    trivial_magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    ]
    min_cost = 10 ** 5  # random big number for min usage
    m = []

    for _ in range(3):
        m.append(list(map(int, input().rstrip().split())))

    for k in range(len(trivial_magic_squares)):
        magic_square = trivial_magic_squares[k]
        cost = 0

        for i in range(3):
            for j in range(3):
                cost += abs(magic_square[i][j] - m[i][j])

        min_cost = min(min_cost, cost)

    print(min_cost)


if __name__ == "__main__":
    main()
