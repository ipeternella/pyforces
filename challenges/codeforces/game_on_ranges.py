import os
import sys


def reverse_moves(alice_picks, n):
    picks = set()
    alice_picks = sorted(alice_picks, key=(lambda pair: abs(pair[0] - pair[1])))

    for l, r in alice_picks:
        if l == r:
            print(l, r, l)
            picks.add((l, r))
        else:
            max_diff = -1
            for l_set, r_set in picks:
                if l_set == l or r_set == r:
                    if abs(r_set - l_set) > max_diff:
                        s_l, s_r = l_set, r_set
                        max_diff = abs(r_set - l_set)

            if s_l == l:
                print(l, r, min(s_r + 1, n))
            elif s_r == r:
                print(l, r, max(s_l - 1, 1))

            picks.add((l, r))


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    t = int(input())
    alice_picks = []

    for _ in range(t):
        n = int(input())
        alice_picks = [tuple(map(int, input().split())) for _ in range(n)]

        reverse_moves(alice_picks, n)
