"""
Solution for: F - LCS

https://atcoder.jp/contests/dp/tasks/dp_f
"""
import os
import sys
from io import StringIO

if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    s, t = input(), input()
    m, n = len(s), len(t)
    buffer = StringIO()

    # state: dp[m][n] where dp[i][j] includes the prefixes of s[1..i], t[1..j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    traceback = [[0] * (n + 1) for _ in range(m + 1)]  # 1: upper left, 2: up, 3: left

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                traceback[i][j] = 1
            else:
                # do not include s[i] or s[j]: pick max lcs so far
                # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    traceback[i][j] = 2
                else:
                    dp[i][j] = dp[i][j - 1]
                    traceback[i][j] = 3

    # traceback and print lcs
    i, j = m, n
    while i > 0 and j > 0:
        if traceback[i][j] == 1:
            buffer.write(s[i - 1])
            i -= 1
            j -= 1
        elif traceback[i][j] == 2:
            i -= 1
        elif traceback[i][j] == 3:
            j -= 1

    print(buffer.getvalue()[::-1])
