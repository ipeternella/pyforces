import os
import sys


def main():
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    # >>> CODE <<< #


if __name__ == "__main__":
    main()
