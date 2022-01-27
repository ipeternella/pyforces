"""
Solution for LC#1305: All Elements in Two Binary Search Trees

https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node, nodes):
            if not node:
                return

            dfs(node.left, nodes)
            nodes.append(node.val)
            dfs(node.right, nodes)

        nodes_1: List[int] = []
        nodes_2: List[int] = []
        dfs(root1, nodes_1)
        dfs(root2, nodes_2)

        return sorted(nodes_1 + nodes_2)
