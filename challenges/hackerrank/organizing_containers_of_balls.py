"""
Solution for: Organizing Containers of Balls

https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
"""
import os
import sys


def main():
    q = int(input())

    for _ in range(q):
        n = int(input())
        containers = []

        for _ in range(n):
            containers.append(list(map(int, input().split())))

        ball_types = [0] * n  # qty of each ball type
        containers_balls = [0] * n  # qty of balls per container (such qty never changes on swaps)

        for i in range(n):
            balls = 0
            for j in range(n):
                # each box
                ball_types[j] += containers[i][j]
                balls += containers[i][j]

            containers_balls[i] = balls

        # qty of each ball type and the container's initial ball quantities must match or it's impossible
        ball_types = sorted(ball_types)
        containers_balls = sorted(containers_balls)
        possible = True

        for i in range(n):
            if ball_types[i] != containers_balls[i]:
                possible = False
                break

        if possible:
            print("Possible")
        else:
            print("Impossible")


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
