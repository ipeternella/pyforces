"""
Solution for: D - Knapsack 1

https://atcoder.jp/contests/dp/tasks/dp_d
"""
import os
import sys

if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    N, W = list(map(int, input().split()))
    items = []

    for _ in range(N):
        w, v = list(map(int, input().split()))
        items.append((w, v))

    # state: dp[up until ith item][bag of weight] = value
    dp = [[0] * (W + 1) for _ in range(N + 1)]  # bag of N items: (n + 1)
    for i in range(1, N + 1):
        w_i, v_i = items[i - 1]
        for w in range(W + 1):
            if w < w_i:
                dp[i][w] = dp[i - 1][w]
            elif w_i <= w:
                # w >= w_i: bag can hold curr item (w_i, v_i) plus another item of (w - w_i): pick it or not!
                # dp[i - 1][w]: previous optimal value for a bag of w weight -> don't pick curr item (w_i, vi)
                # dp[i - 1][w - w_i] + vi: pick the current item with (w_i, v_i) along its previous optimal value
                other_v = w - w_i
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][other_v] + v_i)

    print(dp[N][W])
