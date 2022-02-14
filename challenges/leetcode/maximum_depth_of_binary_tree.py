"""
Solution for LC#104: Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return 0

            left_nodes = dfs(root.left)
            right_nodes = dfs(root.right)

            return max(left_nodes, right_nodes) + 1

        return dfs(root)
