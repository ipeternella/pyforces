import unittest
from unittest import mock
from unittest.mock import call

from powers.binary_tree_traversals import TreeNode
from powers.binary_tree_traversals import bfs
from powers.binary_tree_traversals import dfs_inorder
from powers.binary_tree_traversals import dfs_postorder
from powers.binary_tree_traversals import dfs_preorder


class BinaryTreeTraversalTests(unittest.TestCase):
    @mock.patch("builtins.print")
    def test_should_bfs_binary_tree_inorder(self, mock_print: mock.MagicMock):
        # arrange
        root = self.build_test_bstree_1()

        # act
        bfs(root)

        # assert
        expected_nodes = [call(4), call(2), call(5), call(1), call(3)]
        mock_print.assert_has_calls(expected_nodes)

    @mock.patch("builtins.print")
    def test_should_dfs_binary_tree_inorder(self, mock_print: mock.MagicMock):
        # arrange
        root = self.build_test_bstree_1()

        # act
        dfs_inorder(root)

        # assert
        expected_nodes = [call(1), call(2), call(3), call(4), call(5)]
        mock_print.assert_has_calls(expected_nodes)

    @mock.patch("builtins.print")
    def test_should_dfs_binary_tree_preorder(self, mock_print: mock.MagicMock):
        # arrange
        root = self.build_test_bstree_1()

        # act
        dfs_preorder(root)

        # assert
        expected_nodes = [call(4), call(2), call(1), call(3), call(5)]
        mock_print.assert_has_calls(expected_nodes)

    @mock.patch("builtins.print")
    def test_should_dfs_binary_tree_postorder(self, mock_print: mock.MagicMock):
        # arrange
        root = self.build_test_bstree_1()

        # act
        dfs_postorder(root)

        # assert
        expected_nodes = [call(1), call(3), call(2), call(5), call(4)]
        mock_print.assert_has_calls(expected_nodes)

    def build_test_bstree_1(self) -> TreeNode:
        r"""
            4
           / \
          2   5
         / \
        1   3
        """
        leaf_1 = TreeNode(1)
        leaf_3 = TreeNode(3)
        leaf_5 = TreeNode(5)
        node_2 = TreeNode(2, leaf_1, leaf_3)
        root = TreeNode(4, node_2, leaf_5)

        return root
