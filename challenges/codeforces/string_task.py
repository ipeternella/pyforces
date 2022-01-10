import os
import sys


def process_string(s: str):
    vowels = ["a", "o", "y", "e", "u", "i"]
    n = len(s)

    for i in range(n):
        ch = s[i]

        if ch not in vowels and ch.lower() not in vowels:
            print(f".{ch.lower()}", end="")


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    s = input().rstrip()
    process_string(s)
