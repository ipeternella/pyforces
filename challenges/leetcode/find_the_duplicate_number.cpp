/*
 * Solution for LC#287: Find the Duplicate Number
 *
 * https://leetcode.com/problems/find-the-duplicate-number/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int m = nums.size();
        int n = m - 1;

        // binary search on an imaginary array from [1, 2, 3, .., n]
        int l = 1;
        int r = n;
        int mid = (l + r) / 2;
        int count = 0;

        // O(N*logN)
        while (l <= r) {
            count = 0;
            mid = (l + r) / 2;  // mid of the imaginary sorted array of [l, r]

            // use the original array just to count the numbers
            for (int i = 0; i < m; i++) {
                if (nums[i] <= mid)
                    count++;
            }

            if (count > mid) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return count > mid ? mid : mid + 1;
    }
};
