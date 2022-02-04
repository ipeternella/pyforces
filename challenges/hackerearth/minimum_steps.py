"""
Solution for: Minimum Steps

https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/yogi-and-his-steps-65b27a4b/

[!]: There are test cases whose inputs do not match the problem's description.
"""
import bisect
import os
import sys


# LIS problem in O(N*logN) as 1 <= N <= 5 * 10 ^ 5 so DP solution in O(N^2) is not enough
def lis(arr):
    n = len(arr)
    lis = [0] * (n + 1)
    lis[0] = arr[0]
    size = 1

    for i in range(n):
        if arr[i] > lis[size - 1]:
            lis[size] = arr[i]
            size += 1
        else:
            replace_i = bisect.bisect_left(lis, arr[i], 0, size - 1)
            lis[replace_i] = arr[i]

    return size


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    lis_size = lis(arr)
    lds_size = lis(arr[::-1])  # longest decreasing sequence: lis of reversed arr

    print(min(n - lis_size, n - lds_size))


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
