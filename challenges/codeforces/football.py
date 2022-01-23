import os
import sys


def is_dangerous(s, k):
    n = len(s)
    for i in range(n - k + 1):
        dangerous = True
        for j in range(i, i + k):
            if s[i] != s[j]:
                dangerous = False
                break

        if dangerous:
            return True

    return False


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    s = input()
    k = 7
    print("YES") if is_dangerous(s, k) else print("NO")
