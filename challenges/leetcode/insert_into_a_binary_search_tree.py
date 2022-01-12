"""
Solution for LC#701: Insert into a Binary Search Tree

https://leetcode.com/problems/insert-into-a-binary-search-tree/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs_insert(node, parent):
            if node is None:
                if val > parent.val:
                    parent.right = TreeNode(val)
                else:
                    parent.left = TreeNode(val)

            elif val > node.val:
                dfs_insert(node.right, node)
            else:
                dfs_insert(node.left, node)

        if root is None:
            return TreeNode(val)

        dfs_insert(root, None)
        return root


class SolutionIterative:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        node, parent = root, None
        while node is not None:
            if val > node.val:
                parent = node
                node = node.right
            else:
                parent = node
                node = node.left

        if val > parent.val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)

        return root
