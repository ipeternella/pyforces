/*
 * Solution for LC#51: N-Queens
 *
 * https://leetcode.com/problems/n-queens/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> solutions;

    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> board(n, vector<string>(n, "."));
        place_queens_backtrack(board);

        return solutions;
    }

    void place_queens_backtrack(vector<vector<string>>& board, int queens = 0, int r = 0) {
        int n = board.size();

        if (queens == n) {
            register_solution(board);
            return;
        }

        for (int c = 0; c < n; c++) {
            if (is_free(board, r, c)) {
                board[r][c] = "Q";                                 // place new queen
                place_queens_backtrack(board, queens + 1, r + 1);  // one queen per row only

                // backtrack -- remove placed queen
                board[r][c] = ".";
            }
        }
    }

    bool is_free(vector<vector<string>>& board, int r_b, int c_b) {
        int n = board.size();
        int r, c;

        // above rows check
        for (int r = 0; r < n; r++) {
            if (board[r][c_b] == "Q")
                return false;
        }

        // upper-left diag
        for (r = r_b - 1, c = c_b - 1; r >= 0 && c >= 0; r--, c--) {
            if (board[r][c] == "Q")
                return false;
        }

        // upper-right diag
        for (r = r_b - 1, c = c_b + 1; r >= 0 && c < n; r--, c++) {
            if (board[r][c] == "Q")
                return false;
        }

        return true;
    }

    void register_solution(vector<vector<string>>& board) {
        int n = board.size();
        vector<string> row(n, "");

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (board[r][c] != "Q")
                    row[r].push_back('.');
                else
                    row[r].push_back('Q');
            }
        }

        solutions.push_back(row);
    }
};
