"""
Solution for: ACM ICPC Team

https://www.hackerrank.com/challenges/acm-icpc-team/problem
"""
import os
import sys


def main():
    n, _ = map(int, input().split())
    topics = []
    for _ in range(n):
        topics.append(int(input(), 2))

    teams = 0
    max_topics = 0

    # submitted with Pypy, complexity: O(N^2*logM)
    for i in range(n):
        for j in range(i + 1, n):
            t = 0
            prev_max = max_topics
            combination = topics[i] | topics[j]

            while combination:
                if combination & 1:
                    t += 1
                combination >>= 1

            max_topics = max(max_topics, t)
            if prev_max != max_topics:
                teams = 0

            if t == max_topics:
                teams += 1

    print(max_topics)
    print(teams)


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
