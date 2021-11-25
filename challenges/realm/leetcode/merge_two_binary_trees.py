"""
Solution for LC#617: Merge Two Binary Trees

https://leetcode.com/problems/merge-two-binary-trees/
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs_merge(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
            q = deque()
            q.append((root1, root2, None, False))

            while q:
                node1, node2, parent, left_child = q.popleft()

                if node1 and node2:
                    node1.val += node2.val

                    q.append((node1.left, node2.left, node1, True))
                    q.append((node1.right, node2.right, node1, False))

                elif not node1 and node2:
                    new_node1 = TreeNode(node2.val)

                    if root1 is None:  # root1 was an empty tree, so parent is None
                        root1 = new_node1
                    else:
                        if left_child:
                            parent.left = new_node1
                        else:
                            parent.right = new_node1

                    q.append((None, node2.left, new_node1, True))
                    q.append((None, node2.right, new_node1, False))

            return root1

        if not root2:
            return root1

        root1 = bfs_merge(root1, root2)  # mutates tree1
        return root1
