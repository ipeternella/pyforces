"""
Solution for: A - Frog 1

https://atcoder.jp/contests/dp/tasks/dp_a
"""
import os
import sys

if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    n = int(input())
    h = list(map(int, input().rstrip().split()))

    # state: dp[stone] = min_cost
    dp = [0] * (n)
    dp[1] = abs(h[0] - h[1])

    for i in range(2, n):
        dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))

    print(dp[n - 1])
