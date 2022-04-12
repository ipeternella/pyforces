/*
 * Solution for LC#1260: Shift 2D Grid
 *
 * https://leetcode.com/problems/shift-2d-grid/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        int last1 = 0;
        int last2 = 0;

        k %= m * n;  // anything beyond m * n is redundant
        for (int i = 0; i < k; i++) {
            for (int r = 0; r < m; r++) {
                last1 = grid[r][n - 1];

                for (int c = n - 1; c > 0; c--)
                    grid[r][c] = grid[r][c - 1];

                if (r == 0)
                    grid[0][0] = m > 1 ? grid[m - 1][n - 1] : last1;
                else
                    grid[r][0] = last2;

                last2 = last1;
            }
        }

        return grid;
    }
};
