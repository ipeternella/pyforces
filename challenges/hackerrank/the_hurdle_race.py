import os
import sys

if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    n, k = list(map(int, input().rstrip().split()))
    h = list(map(int, input().rstrip().split()))
    max_h = max(h)
    potions = 0

    print(max(0, max_h - k))
