"""
Solution for LC#450: Delete Node in a BST

https://leetcode.com/problems/delete-node-in-a-bst/
"""

from typing import Optional
from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(
    node: Optional[TreeNode], key: int, parent: Optional[TreeNode] = None
) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
    if node is None:
        return None, None

    if key > node.val:
        return dfs(node.right, key, node)
    elif key < node.val:
        return dfs(node.left, key, node)
    else:
        return node, parent


def dfs_min(
    node: Optional[TreeNode], parent: Optional[TreeNode] = None
) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
    if node is None:
        return None, None

    if node.left is None:
        return node, parent

    return dfs_min(node.left, node)


def update_parent_child(
    old_node: Optional[TreeNode], old_parent: Optional[TreeNode], new_node: Optional[TreeNode]
) -> None:
    if old_parent is None:  # root
        return

    if old_node == old_parent.left:
        old_parent.left = new_node
    else:
        old_parent.right = new_node


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        target, target_parent = dfs(root, key)
        if target is None:
            return root

        if target.left is None:
            update_parent_child(target, target_parent, new_node=target.right)
            if target_parent is None:
                root = target.right

        elif target.right is None:
            update_parent_child(target, target_parent, new_node=target.left)
            if target_parent is None:
                root = target.left

        else:
            successor, sucessor_parent = dfs_min(target.right, target)
            if sucessor_parent != target:
                # used to 'unplug' the successor from the tree to avoid cyclic references
                # so we swap the successor with its right child easily (successor has NO left child, it's a min)
                update_parent_child(successor, sucessor_parent, new_node=successor.right)  # type: ignore
                successor.right = target.right  # type: ignore

            update_parent_child(target, target_parent, new_node=successor)
            successor.left = target.left  # type: ignore
            if target_parent is None:
                root = successor

        return root
