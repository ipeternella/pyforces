/*
 * Solution for LC#669: Trim a Binary Search Tree
 *
 * https://leetcode.com/problems/trim-a-binary-search-tree/
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
    TreeNode* trimBST(TreeNode* root, int low, int high) {
        queue<pair<TreeNode*, TreeNode*>> q;
        TreeNode* new_root = nullptr;
        q.push({root, nullptr});  // no parent in the beginning

        while (!q.empty()) {
            pair<TreeNode*, TreeNode*> p = q.front();
            TreeNode* curr = p.first;
            TreeNode* parent = p.second;
            q.pop();

            if (curr->val < low) {
                trim_parent(parent, curr);
                if (curr->right)
                    q.push({curr->right, parent});
            } else if (curr->val > high) {
                trim_parent(parent, curr);
                if (curr->left)
                    q.push({curr->left, parent});
            } else {
                if (!parent)
                    new_root = curr;
                else
                    link_parent(parent, curr);

                parent = curr;
                if (curr->left)
                    q.push({curr->left, parent});

                if (curr->right)
                    q.push({curr->right, parent});
            }
        }

        return new_root;
    }

    void trim_parent(TreeNode* parent, TreeNode* curr) {
        if (!parent)
            return;

        if (parent->val > curr->val) {
            parent->left = nullptr;
        } else {
            parent->right = nullptr;
        }
    }

    void link_parent(TreeNode* parent, TreeNode* curr) {
        if (!parent)
            return;

        if (curr->val <= parent->val) {
            parent->left = curr;
        } else {
            parent->right = curr;
        }
    }
};
