/*
 * Solution for LC#718: Maximum Length of Repeated Subarray
 *
 * https://leetcode.com/problems/maximum-length-of-repeated-subarray/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findLength(vector<int>& n2, vector<int>& n1) {
        int m = n1.size();
        int n = n2.size();
        int longest = 0;
        vector<vector<int>> dp(m + 1, vector<int>(n + 1));

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0)
                    continue;

                if (n1[i - 1] == n2[j - 1]) {
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1);
                    longest = max(longest, dp[i][j]);
                } else {
                    // unlike in LCS, as we are dealing with subarrays and not subsequences,
                    // if two numbers do not match, subarray length gets zero as there's no
                    // more continuity required by subarrays
                    dp[i][j] = 0;
                }
            }
        }

        return longest;
    }
};
