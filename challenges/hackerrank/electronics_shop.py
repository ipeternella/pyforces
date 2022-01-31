import os
import sys

if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    b, n, m = list(map(int, input().split()))
    keyboards = sorted(list(map(int, input().split())))
    drives = sorted(list(map(int, input().split())))

    best = -1
    l = 0
    r = m - 1
    while r >= 0 and l <= n - 1:
        purchase = keyboards[l] + drives[r]

        if purchase <= b:
            best = max(best, purchase)

        if purchase > b:
            r -= 1
        elif purchase < b:
            l += 1
        else:
            break

    print(best)
