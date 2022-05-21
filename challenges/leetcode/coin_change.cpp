/*
 * Solution for LC#322: Coin Change
 *
 * https://leetcode.com/problems/coin-change/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // dp[value] = coins
        vector<long> dp(amount + 1, INT_MAX - 1);

        // init state
        dp[0] = 0;

        // bottom-up dp
        for (long val = 0; val <= amount; val++) {
            for (long coin : coins) {
                if (val + coin <= amount) {
                    dp[val + coin] = min(dp[val + coin], dp[val] + 1);
                }
            }
        }

        return dp[amount] == INT_MAX - 1 ? -1 : dp[amount];
    }
};
