/*
 * Solution for LC#1091: Shortest Path in Binary Matrix
 *
 * https://leetcode.com/problems/shortest-path-in-binary-matrix/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        queue<pair<int, int>> Q;
        vector<vector<int>> dists(n, vector<int>(n, INT_MAX));

        // bfs
        if (grid[0][0] != 1 and grid[n - 1][n - 1] != 1) {
            dists[0][0] = 1;
            Q.push({0, 0});
        }

        while (!Q.empty()) {
            int r = Q.front().first;
            int c = Q.front().second;
            Q.pop();
            grid[r][c] = -1;  // visited

            auto adj_nodes = get_valid_adj_nodes(grid, r, c);
            for (auto adj : adj_nodes) {
                int r_adj = adj.first;
                int c_adj = adj.second;

                // excludes 1s and visited nodes -1
                if (dists[r][c] + 1 < dists[r_adj][c_adj]) {
                    dists[r_adj][c_adj] = dists[r][c] + 1;
                    Q.push({r_adj, c_adj});
                }
            }
        }

        return dists[n - 1][n - 1] == INT_MAX ? -1 : dists[n - 1][n - 1];
    }

    vector<pair<int, int>> get_valid_adj_nodes(vector<vector<int>>& grid, int r, int c) {
        vector<pair<int, int>> adj;
        int n = grid.size();

        // must be within the board and not have been visited
        for (int i = r - 1; i <= r + 1; i++) {
            for (int j = c - 1; j <= c + 1; j++) {
                if (i >= 0 and i < n and j >= 0 and j < n and grid[i][j] == 0) {
                    adj.push_back({i, j});
                }
            }
        }

        return adj;
    }
};
