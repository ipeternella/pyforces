/*
 * Solution for LC#289: Game of Life
 *
 * https://leetcode.com/problems/game-of-life/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();

        // solution with in-place changes: time complexity: O(m*n), space complexity: O(1)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                pair<int, int> p = scan_cell(board, i, j);
                int zeros = p.first;
                int ones = p.second;

                // "-1" represents a living cell that died but for state computation: remains 1
                if (board[i][j] == 1) {
                    if (ones < 2)
                        board[i][j] = -1;  // under-pop
                    else if (ones > 3)
                        board[i][j] = -1;  // over-pop
                }

                // "2" represents a cell that was reproduced but for state computation remains 0
                if (board[i][j] == 0) {
                    if (ones == 3)
                        board[i][j] = 2;
                }
            }
        }

        // post-process to fix in-place changes with intermediary states (fix -1 and 2 to their states: 0 or 1)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == -1)
                    board[i][j] = 0;  // 1 -> 0

                if (board[i][j] == 2)
                    board[i][j] = 1;  // 0 -> 1
            }
        }
    }

    pair<int, int> scan_cell(vector<vector<int>>& board, int i, int j) {
        int m = board.size();
        int n = board[0].size();
        int ones = 0;
        int zeros = 0;

        auto neighbors = get_neighbors(i, j, m, n);
        for (auto p : neighbors) {
            int r = p.first;
            int c = p.second;

            if (board[r][c] == 0 or board[r][c] == 2)  // 2 was a previous 0
                zeros++;

            if (board[r][c] == 1 or board[r][c] == -1)  // -1 was a previous 1
                ones++;
        }

        return make_pair(zeros, ones);
    }

    vector<pair<int, int>> get_neighbors(int i, int j, int m, int n) {
        vector<pair<int, int>> neighbors;

        if (i + 1 < m) {
            neighbors.push_back({i + 1, j});

            // upper diags
            if (j + 1 < n)
                neighbors.push_back({i + 1, j + 1});

            if (j - 1 >= 0)
                neighbors.push_back({i + 1, j - 1});
        }

        if (i - 1 >= 0) {
            neighbors.push_back({i - 1, j});

            // lower diags
            if (j + 1 < n)
                neighbors.push_back({i - 1, j + 1});

            if (j - 1 >= 0)
                neighbors.push_back({i - 1, j - 1});
        }

        if (j + 1 < n)
            neighbors.push_back({i, j + 1});

        if (j - 1 >= 0)
            neighbors.push_back({i, j - 1});

        return neighbors;
    }
};
