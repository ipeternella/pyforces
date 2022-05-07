/*
 * Solution for LC#1679: Max Number of K-Sum Pairs
 *
 * https://leetcode.com/problems/max-number-of-k-sum-pairs/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        int n = nums.size();
        int ops = 0;

        // sorting + two pointers: O(n*logn)
        int l = 0;
        int r = n - 1;
        sort(nums.begin(), nums.end());
        while (l < r) {
            int sum = nums[l] + nums[r];

            if (sum > k) {
                r--;
            } else if (sum < k) {
                l++;
            } else {
                ops++;
                l++;
                r--;
            }
        }

        return ops;
    }
};
