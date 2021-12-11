"""
Solution for: Binary Search Tree : Insertion

https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
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


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val: int) -> None:
        def helper(node: Optional[Node]) -> None:
            if node is None:
                self.root = Node(info=val)

            elif val > node.info and node.right is None:
                node.right = Node(info=val)

            elif val <= node.info and node.left is None:
                node.left = Node(info=val)

            elif val > node.info:
                helper(node.right)

            else:
                helper(node.left)

        helper(self.root)
