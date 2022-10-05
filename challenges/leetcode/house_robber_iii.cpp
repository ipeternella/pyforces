/*
 * Solution for LC#337: House Robber III
 *
 * https://leetcode.com/problems/house-robber-iii/
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
    int rob(TreeNode* root) {
        unordered_map<TreeNode*, unordered_map<bool, int>> memo;
        return dfs(root, memo, false);  // dp on trees with hashmap (slower) but stores pointers
    }

    int dfs(TreeNode* root, unordered_map<TreeNode*, unordered_map<bool, int>>& memo, bool taken) {
        if (!root)
            return 0;

        if (memo.find(root) != memo.end() and memo[root].find(taken) != memo[root].end())
            return memo[root][taken];

        if (taken) {
            return memo[root][taken] = dfs(root->left, memo, false) + dfs(root->right, memo, false);
        } else {
            int take = root->val + dfs(root->left, memo, true) + dfs(root->right, memo, true);
            int dont = dfs(root->left, memo, false) + dfs(root->right, memo, false);

            return memo[root][taken] = max(take, dont);
        }
    }
};
