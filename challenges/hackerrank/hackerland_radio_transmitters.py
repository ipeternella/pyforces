import os
import sys

if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    n, k = list(map(int, input().split()))
    h = sorted(list(map(int, input().split())))
    covered = False
    hlimit = h[0] + k
    transmitters = 0

    for i in range(n):
        if h[i] > hlimit and covered:  # house marks a new house to start counting from there
            covered = False
            hlimit = h[i] + k
        elif h[i] > hlimit:
            transmitters += 1  # antenna at h[i - 1] house
            hlimit = h[i - 1] + k

            if h[i] <= hlimit:
                covered = True
            else:
                hlimit = h[i] + k
                covered = False

    if not covered:
        transmitters += 1

    print(transmitters)
