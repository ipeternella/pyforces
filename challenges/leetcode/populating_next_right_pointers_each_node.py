"""
Solution for LC#116: Populating Next Right Pointers in Each Node

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""
from collections import deque
from typing import Deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional["Node"]) -> Optional["Node"]:
        if root is None:
            return None

        q: Deque["Node"] = deque()
        q.append(root)

        # constant space besides BFS queue
        node_ahead = None
        level = 0
        remaining = 1

        while q:
            node = q.popleft()

            if node.right:
                q.append(node.right)

            if node.left:
                q.append(node.left)

            node.next = node_ahead
            if remaining < 2:  # last node on the level -> reset node_ahead
                level += 1
                remaining = 2 ** level
                node_ahead = None
            else:
                node_ahead = node
                remaining -= 1

        return root
