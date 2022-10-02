/*
 * Solution for LC#213: House Robber II
 *
 * https://leetcode.com/problems/house-robber-ii/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n + 1);
        int ans = 0;

        // take first house
        dp[1] = nums[0];
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1];
            if (i - 2 >= 0 and i < n)  // cant take last house
                dp[i] = max(dp[i], dp[i - 2] + nums[i - 1]);
        }
        ans = dp[n];

        // dont take first house
        dp[1] = 0;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1];
            if (i - 2 >= 0)
                dp[i] = max(dp[i], dp[i - 2] + nums[i - 1]);
        }

        // pick max
        return max(ans, dp[n]);
    }
};
