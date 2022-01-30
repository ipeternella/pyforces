import os
import sys

if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    q = int(input())
    for _ in range(q):
        cat_a, cat_b, mouse = list(map(int, input().split()))

        if abs(cat_a - mouse) < abs(cat_b - mouse):
            print("Cat A")
        elif abs(cat_a - mouse) > abs(cat_b - mouse):
            print("Cat B")
        else:
            print("Mouse C")
