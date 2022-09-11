/*
 * Solution for LC#37: Sudoku Solver
 *
 * https://leetcode.com/problems/sudoku-solver/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    const char EMPTY = '.';

    void solveSudoku(vector<vector<char>>& board) {
        solve(board);
    }

    bool solve(vector<vector<char>>& board, int r = 0, int c = 0) {
        int n = board.size();
        if (r > n - 1)
            return true;
        if (c > n - 1)
            return solve(board, r + 1, 0);
        if (board[r][c] != EMPTY)
            return solve(board, r, c + 1);

        // check if move is valid now and valid later: backtrack if needed
        for (int d = 1; d <= 9; d++) {
            board[r][c] = '0' + d;  // make a new move
            if (!valid_move(board, r, c) or !solve(board, r, c + 1)) {
                board[r][c] = EMPTY;  // backtrack and try again if move is not valid
            } else {
                return true;
            }
        }

        return false;  // exhausted all possibilities
    }

    bool valid_move(vector<vector<char>>& board, int r, int c) {
        return valid_row(board, r) and valid_col(board, c) and valid_box(board, r, c);
    }

    bool valid_row(vector<vector<char>>& board, int r) {
        int n = board.size();
        vector<int> f(10);
        for (int c = 0; c < n; c++) {
            char slot = board[r][c];
            if (slot == EMPTY)
                continue;
            int i = slot - '0';
            f[i]++;
        }
        for (int i = 0; i < 10; i++)
            if (f[i] > 1)
                return false;
        return true;
    }

    bool valid_col(vector<vector<char>>& board, int c) {
        int n = board.size();
        vector<int> f(10);
        for (int r = 0; r < n; r++) {
            char slot = board[r][c];
            if (slot == EMPTY)
                continue;
            int i = slot - '0';
            f[i]++;
        }
        for (int i = 0; i < 10; i++)
            if (f[i] > 1)
                return false;
        return true;
    }

    bool valid_box(vector<vector<char>>& board, int r, int c) {
        int c_start = 3 * (c / 3);
        int r_start = 3 * (r / 3);
        vector<int> f(10);
        for (int r = r_start; r < r_start + 3; r++) {
            for (int c = c_start; c < c_start + 3; c++) {
                char slot = board[r][c];
                if (slot == EMPTY)
                    continue;

                int i = slot - '0';
                f[i]++;
            }
        }
        for (int i = 0; i < 10; i++)
            if (f[i] > 1)
                return false;
        return true;
    }
};
