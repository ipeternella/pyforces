/*
 * Solution for LC#583: Delete Operation for Two Strings
 *
 * https://leetcode.com/problems/delete-operation-for-two-strings/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));

        // delete all chars from two strings until they become the same (even if just two empty strings)
        // hence, we remove all chars from each str that are diff from lcs
        int lcs_result = lcs(word1, word2, m, n, dp);
        return m + n - 2 * lcs_result;
    }

    int lcs(string& s1, string& s2, int m, int n, vector<vector<int>>& dp) {
        // no more common chars
        if (m == 0 or n == 0) {
            return 0;
        }

        // overlapping subproblem has already been solved
        if (dp[m][n] != -1) {
            return dp[m][n];
        }

        // same char add 1 more common char to lcs
        if (s1[m - 1] == s2[n - 1]) {
            return dp[m][n] = lcs(s1, s2, m - 1, n - 1, dp) + 1;
        }

        // branch into two subproblems: remove one char from each substr and get the max
        return dp[m][n] = max(lcs(s1, s2, m - 1, n, dp), lcs(s1, s2, m, n - 1, dp));
    }
};
