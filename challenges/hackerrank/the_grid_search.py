"""
Solution for: The Grid Search

https://www.hackerrank.com/challenges/the-grid-search/problem
"""
import os
import sys


def square_scan(g, p, r_g, c_g, r_p, c_p):
    for r in range(r_g - r_p + 1):
        for c in range(c_g - c_p + 1):
            rows_match = True
            columns_match = True

            for j in range(c_p):
                for i in range(r_p):
                    if g[r + i][c + j] != p[i][j]:
                        rows_match = False
                        break

                if not rows_match:
                    columns_match = False
                    break

            if rows_match and columns_match:
                return True

    return False


def main():
    t = int(input())

    for _ in range(t):
        r_g, c_g = map(int, input().rstrip().split())
        g = ["" for _ in range(r_g)]
        for i in range(r_g):
            g[i] = input()

        r_p, c_p = map(int, input().rstrip().split())
        p = ["" for _ in range(r_p)]
        for i in range(r_p):
            p[i] = input()

        if square_scan(g, p, r_g, c_g, r_p, c_p):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
