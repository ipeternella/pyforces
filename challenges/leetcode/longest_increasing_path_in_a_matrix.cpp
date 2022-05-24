/*
 * Solution for LC#329: Longest Increasing Path in a Matrix
 *
 * https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int max_len;

    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, -1));  // dp[row][col] = LIP
        max_len = 1;

        // DFS with dynamic programming (memoized approach)
        dp[0][0] = 1;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                dfs(matrix, dp, r, c);
            }
        }

        return max_len;
    }

    int dfs(vector<vector<int>>& matrix, vector<vector<int>>& dp, int r, int c) {
        auto adjs = get_adj(matrix, r, c);

        for (auto adj : adjs) {
            if (dp[adj.first][adj.second] == -1) {  // LIP not found in memo
                dp[r][c] = max(dp[r][c], dfs(matrix, dp, adj.first, adj.second) + 1);
            } else {
                dp[r][c] = max(dp[r][c], dp[adj.first][adj.second] + 1);  // use previous state in memo
            }

            max_len = max(max_len, dp[r][c]);
        }

        // if not bigger than any adj value -> min possible LIP is one
        if (dp[r][c] == -1) {
            dp[r][c] = 1;
        }

        return dp[r][c];
    }

    vector<pair<int, int>> get_adj(vector<vector<int>>& matrix, int r, int c) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<pair<int, int>> adjs;

        if (r - 1 >= 0 and matrix[r - 1][c] > matrix[r][c]) {
            adjs.push_back({r - 1, c});
        }

        if (r + 1 < m and matrix[r + 1][c] > matrix[r][c]) {
            adjs.push_back({r + 1, c});
        }

        if (c - 1 >= 0 and matrix[r][c - 1] > matrix[r][c]) {
            adjs.push_back({r, c - 1});
        }

        if (c + 1 < n and matrix[r][c + 1] > matrix[r][c]) {
            adjs.push_back({r, c + 1});
        }

        return adjs;
    }
};
