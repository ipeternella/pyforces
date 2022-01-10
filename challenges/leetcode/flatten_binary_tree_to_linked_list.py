"""
Solution for LC#114: Flatten Binary Tree to Linked List

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs_postorder(node):
            nonlocal last_right_node

            if node is None:
                return

            dfs_postorder(node.right)
            dfs_postorder(node.left)

            node.right = last_right_node
            node.left = None
            last_right_node = node

        last_right_node = None
        dfs_postorder(root)
