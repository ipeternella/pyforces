import os
import sys
from typing import List

INF = sys.maxsize


def recompute_ratings(ratings: List[int], reactions: List[int]):
    like_ratings, dislike_ratings = [], []
    updated_likes, updated_dislikes = [], []
    indexes = dict()

    for i, r in enumerate(ratings):
        indexes[r] = i

        if reactions[i] == 1:
            like_ratings.append(r)
        else:
            dislike_ratings.append(r)

    like_ratings, dislike_ratings = sorted(like_ratings), sorted(dislike_ratings)
    m, n = len(like_ratings), len(dislike_ratings)
    i, j = m - 1, n - 1

    for _ in range(m):
        rating_like = like_ratings[i]
        rating_dislike = dislike_ratings[j] if j >= 0 else -INF

        if rating_like < rating_dislike:
            updated_likes.append(rating_dislike)
            j -= 1
        else:
            updated_likes.append(rating_like)
            i -= 1

    while i >= 0:
        updated_dislikes.append(like_ratings[i])
        i -= 1

    while j >= 0:
        updated_dislikes.append(dislike_ratings[j])
        j -= 1

    updated_dislikes = sorted(updated_dislikes, reverse=True)

    for i in range(len(updated_likes) - 1, -1, -1):
        j = indexes[like_ratings[i]]  # index to mutate (biggest like)
        ratings[j] = updated_likes[m - 1 - i]  #

    for i in range(len(updated_dislikes)):
        j = indexes[dislike_ratings[i]]  # index to mutate (biggest dislike)
        ratings[j] = updated_dislikes[n - 1 - i]

    print(" ".join(map(str, ratings)))


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    t = int(input())
    for _ in range(t):
        _ = int(input())
        ratings = list(map(int, input().rstrip().split()))
        reactions = [int(ch) for ch in input().rstrip()]

        recompute_ratings(ratings, reactions)
