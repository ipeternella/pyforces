"""
Solution for LC#101: Symmetric Tree

https://leetcode.com/problems/symmetric-tree/
"""
from collections import deque as Queue
from typing import List
from typing import Optional
from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionII:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            value1 = node1.val if node1 is not None else None
            value2 = node2.val if node2 is not None else None

            if node1 is None and node2 is None:
                return True

            if value1 != value2:
                return False

            # two pointers traversal at opposite directions
            return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)

        return dfs(root.left, root.right)  # type: ignore


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q: Queue[Tuple[Optional[TreeNode], int]] = Queue()
        q.append((root, 0))
        level_nodes: List[Optional[int]] = []
        prev_level = 0

        # bfs to check each level with double pointers (probably an overkill)
        while q:
            node, level = q.popleft()

            # new level
            if prev_level != level:
                n = len(level_nodes)
                i, j = 0, n - 1
                while i <= j:
                    if level_nodes[i] != level_nodes[j]:
                        return False

                    i += 1
                    j -= 1

                level_nodes = []
                prev_level = level

            level_nodes.append(node.val if node is not None else None)

            if node is not None:
                q.append((node.left, level + 1))
                q.append((node.right, level + 1))

        return True
