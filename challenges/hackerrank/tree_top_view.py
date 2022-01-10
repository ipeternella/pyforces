"""
Solution for: Tree : Top View

https://www.hackerrank.com/challenges/tree-top-view/problem
"""
from collections import deque
from typing import Deque
from typing import Tuple


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def topView(root: Node) -> None:
    right_view = [root.info]
    left_view = []
    q: Deque[Tuple[Node, int, int]] = deque()
    max_l_offset = 0
    max_r_offset = 0

    # bfs based on left/right offsets from the root (root has offset (0,0))
    q.append((root, 0, 0))
    while q:
        node, l_offset, r_offset = q.popleft()

        if node != root:
            if l_offset > max_l_offset:
                max_l_offset = l_offset
                left_view.append(node.info)

            if r_offset > max_r_offset:
                max_r_offset = r_offset
                right_view.append(node.info)

        if node.left is not None:
            q.append((node.left, l_offset + 1, r_offset - 1))

        if node.right is not None:
            q.append((node.right, l_offset - 1, r_offset + 1))

    # view printing
    for view in reversed(left_view):
        print(view, end=" ")

    for view in right_view:
        print(view, end=" ")
