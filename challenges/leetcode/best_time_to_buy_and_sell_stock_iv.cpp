/*
 * Solution for LC#188: Best Time to Buy and Sell Stock IV
 *
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int dp(vector<int>& prices, vector<vector<vector<int>>>& memo, int i, int k, bool buy) {
        int n = prices.size();
        if (i == n or k == 0)
            return 0;

        if (memo[i][buy][k] != -1)
            return memo[i][buy][k];

        // buy this stock at the current price or wait and buy it with the next price
        if (buy) {
            return memo[i][buy][k] =
                       max(-prices[i] + dp(prices, memo, i + 1, k, false), dp(prices, memo, i + 1, k, true));
        }

        // sell the stock now (k - 1 txs left) or hold it to sell later (k txs remain)
        return memo[i][buy][k] =
                   max(prices[i] + dp(prices, memo, i + 1, k - 1, true), dp(prices, memo, i + 1, k, false));
    }

    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        vector<vector<vector<int>>> memo(n + 1, vector<vector<int>>(2, vector<int>(k + 1, -1)));

        return dp(prices, memo, 0, k, true);
    }
};
