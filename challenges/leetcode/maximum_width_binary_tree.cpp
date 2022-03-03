/*
 * Solution for LC#662: Maximum Width of Binary Tree
 *
 * https://leetcode.com/problems/maximum-width-of-binary-tree/
 */
#include <bits/stdc++.h>
#define ll long long

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
    int widthOfBinaryTree(TreeNode* root) {
        ll max_width = 1;
        queue<pair<TreeNode*, ll>> q;
        TreeNode* curr;
        pair<TreeNode*, ll> p;

        q.push({root, 0});
        while (!q.empty()) {
            ll level_size = q.size();
            ll left = q.front().second;
            ll right = q.back().second;
            max_width = max(max_width, right - left + 1);

            // traverse all nodes in the current level
            for (int k = 0; k < level_size; k++) {
                p = q.front();
                curr = p.first;

                // width is based on diffs so always shift indexes left to avoid int overflows
                ll j = p.second - left;
                q.pop();

                if (curr->left)
                    q.push({curr->left, 2 * j});

                if (curr->right)
                    q.push({curr->right, 2 * j + 1});
            }
        }

        return (int)max_width;
    }
};
