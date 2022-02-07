"""
Solution for: Non-Divisible Subset

https://www.hackerrank.com/challenges/non-divisible-subset/problem
"""
import os
import sys


def main():
    _, k = map(int, input().rstrip().split())
    s = set(map(int, input().rstrip().split()))

    mod_freqs = [0] * k
    for num in s:
        mod_freqs[num % k] += 1

    # in final the subset, there can only be one num whose num % K == 0,
    # as two nums with remainder 0, when added, will be divisible by K
    mod_freqs[0] = 1 if mod_freqs[0] > 0 else -1

    # if k is even, then x and (k - x) will be the same and will be ignored, so
    # just like num % K == 0, num % k == k // 2 can only appear once as two
    # with same modulo result will by divisible by K
    if k % 2 == 0:
        mod_freqs[k // 2] = 1 if mod_freqs[k // 2] > 0 else -1

    size = 0

    for x in range(1, k):
        if mod_freqs[x] == -1:
            continue
        if k % 2 == 0 and x == k // 2:
            continue  # already handled previously

        if mod_freqs[x] >= mod_freqs[k - x]:
            mod_freqs[k - x] = -1  # x is bigger than k - x, so we pick it and ignore its counter part
        else:
            mod_freqs[x] = -1

    for num in mod_freqs:
        size = size + num if num > 0 else size

    print(size)


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
