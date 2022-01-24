"""
Solution for: B - Frog 2

https://atcoder.jp/contests/dp/tasks/dp_b
"""
import os
import sys

INF = sys.maxsize

if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    n, k = list(map(int, input().split()))
    h = list(map(int, input().rstrip().split()))

    # state: dp[stone] = min_cost
    dp = [INF] * (n)
    dp[0] = 0

    for i in range(1, n):
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + abs(h[i] - h[i - j]))

    print(dp[n - 1])
