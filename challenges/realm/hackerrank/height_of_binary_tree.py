"""
Solution for: Tree: Height of a Binary Tree

https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
"""
from typing import Optional


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def height(root: Optional[Node]) -> int:
    def helper(node: Optional[Node]):
        if node is None:
            return 0

        h = max(helper(node.left), helper(node.right)) + 1
        return h if node != root else h - 1  # -1 when root

    return helper(root)
