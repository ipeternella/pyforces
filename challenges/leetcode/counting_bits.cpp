/*
 * Solution for LC#338: Counting Bits
 *
 * https://leetcode.com/problems/counting-bits/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp(n + 1, 0);
        int pow2 = 1, last_pow2 = 1;

        for (int i = 1; i <= n; i++) {
            if (i == pow2) {
                dp[i] = 1;
                last_pow2 = pow2;
                pow2 *= 2;
            } else {
                dp[i] = 1 + dp[i - last_pow2];
            }
        }

        return dp;
    }
};
