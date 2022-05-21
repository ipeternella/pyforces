/*
 * Solution for LC#63: Unique Paths II
 *
 * https://leetcode.com/problems/unique-paths-ii/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));

        // base state case
        dp[0][0] = 1;

        // bottom-up dynamic programming
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (obstacleGrid[r][c] == 1) {
                    dp[r][c] = 0;
                    continue;
                }

                int up_paths = r - 1 >= 0 and obstacleGrid[r - 1][c] == 0 ? dp[r - 1][c] : 0;
                int left_paths = c - 1 >= 0 and obstacleGrid[r][c - 1] == 0 ? dp[r][c - 1] : 0;

                // state transation with state re-use of previous overlapping subproblems
                dp[r][c] = max(dp[r][c], up_paths + left_paths);
            }
        }

        return dp[m - 1][n - 1];
    }
};
