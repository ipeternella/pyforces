/*
 * Solution for LC#1695: Maximum Erasure Value
 *
 * https://leetcode.com/problems/maximum-erasure-value/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_map<int, int> hashmap;
        vector<int> prefixes;
        int n = nums.size();
        int score = 0, max_score = 0;
        int l = 0;

        // prefix sum
        int s = 0;
        for (int i = 0; i < n; i++) {
            s += nums[i];
            prefixes.push_back(s);
        }

        for (int r = 0; r < n; r++) {
            auto check = hashmap.find(nums[r]);

            // found repeated element - sum range of [l, r) using prefixes sum
            // and then update the range to be [j + 1, r] (j == index of repeated num in curr range)
            if (check != hashmap.end() and check->second >= l) {
                int j = check->second;
                score = l == 0 ? prefixes[r - 1] : prefixes[r - 1] - prefixes[l - 1];
                max_score = max(max_score, score);
                l = j + 1;
            } else if (r == n - 1) {  // always sum last subarray [l, n - 1]
                score = l == 0 ? prefixes[r] : prefixes[r] - prefixes[l - 1];
                max_score = max(max_score, score);
            }

            hashmap[nums[r]] = r;
        }

        return max_score;
    }
};
