"""
Solution for: Absolute Permutation

https://www.hackerrank.com/challenges/absolute-permutation/problem
"""
import os
import sys


def find_abs_permutation(n, k):
    options = [1] * (n + 1)
    options[0] = 0
    ans = [-1] * (n + 1)

    for num in range(1, n + 1):
        low = num - k
        high = num + k
        low_available = low >= 1 and options[low] > 0
        high_available = high <= n and options[high] > 0

        if not low_available and not high_available:
            print(-1)
            return

        if low_available and not high_available:
            options[low] -= 1
            ans[num] = low
        elif high_available and not low_available:
            options[high] -= 1
            ans[num] = high

    for num in range(1, n + 1):
        low = num - k
        high = num + k
        low_available = low >= 1 and options[low] > 0
        high_available = high <= n and options[high] > 0

        if low_available and not high_available:
            options[low] -= 1
            ans[num] = low
        elif high_available and not low_available:
            options[high] -= 1
            ans[num] = high
        elif high_available and low_available:
            options[low] -= 1
            ans[num] = low

    print(" ".join(map(str, ans[1:])))


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().rstrip().split())
        find_abs_permutation(n, k)


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
