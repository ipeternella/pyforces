/*
 * Solution for LC#173: Binary Search Tree Iterator
 *
 * https://leetcode.com/problems/binary-search-tree-iterator/
 */
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class BSTIterator {
public:
    vector<TreeNode*> path;

    BSTIterator(TreeNode* root) {
        path.push_back(root);
        dfs_left_path(root);
    }

    int next() {
        TreeNode* curr = path.back();
        path.pop_back();

        // if there's a right child, push it to path and traverse all left subtrees
        if (curr->right) {
            path.push_back(curr->right);
            dfs_left_path(curr->right);
        }

        return curr->val;
    }

    void dfs_left_path(TreeNode* root) {
        if (!root)
            return;

        TreeNode* curr = root->left;
        while (curr) {
            path.push_back(curr);
            curr = curr->left;
        }
    }

    bool hasNext() {
        return path.size() > 0;
    }
};
