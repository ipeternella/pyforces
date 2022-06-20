/*
 * Solution for LC#1048: Longest String Chain
 *
 * https://leetcode.com/problems/longest-string-chain/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(), sort_by_len);

        return lis_str_chain(words);
    }

    int lis_str_chain(vector<string>& words) {
        int n = words.size();
        int lsc = 1;
        vector<int> dp(n + 1, 1);

        // LIS problem for predecessors
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (is_predecessor(words[j], words[i])) {
                    dp[i] = max(dp[i], dp[j] + 1);
                    lsc = max(lsc, dp[i]);
                }
            }
        }

        return lsc;
    }

    // s1 must be a smaller string
    bool is_predecessor(string& s1, string& s2) {
        int m = s1.size();
        int n = s2.size();

        if (n != m + 1)
            return false;

        int i = 0, j = 0;
        while (i < m and j < n) {
            if (s1[i] == s2[j]) {
                i++;
            }

            j++;
        }

        return i == m;
    }

    // sorts strings by their size only
    static bool sort_by_len(string& s1, string& s2) {
        int m = s1.size();
        int n = s2.size();

        return m < n;
    }
};
