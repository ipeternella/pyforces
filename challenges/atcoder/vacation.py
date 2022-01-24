"""
Solution for: C - Vacation

https://atcoder.jp/contests/dp/tasks/dp_c
"""
import os
import sys

INF = sys.maxsize

if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    n = int(input())
    points = []
    for _ in range(n):
        a, b, c = list(map(int, input().rstrip().split()))
        points.append((a, b, c))

    # dp[day][option] = min_cost
    dp = [[-INF] * 3 for _ in range(n)]
    dp[0] = [points[0][0], points[0][1], points[0][2]]

    for i in range(1, n):
        for j in range(3):
            for k in range(3):
                if k != j:
                    # dp[i][j] means for day i, pick option j: so previous day's k != j
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + points[i][j])

    print(max(dp[n - 1]))
