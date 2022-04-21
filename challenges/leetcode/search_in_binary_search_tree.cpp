/*
 * Solution for LC#700: Search in a Binary Search Tree
 *
 * https://leetcode.com/problems/search-in-a-binary-search-tree/
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

class Solution {
public:
    TreeNode* dfs(TreeNode* root, int target) {
        if (!root)
            return nullptr;

        if (root->val == target) {
            return root;
        } else if (target < root->val) {
            return dfs(root->left, target);
        } else {
            return dfs(root->right, target);
        }
    }

    TreeNode* searchBST(TreeNode* root, int val) {
        return dfs(root, val);
    }
};
