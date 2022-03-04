/*
 * Solution for LC#413: Arithmetic Slices
 *
 * https://leetcode.com/problems/arithmetic-slices/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int n = nums.size();
        int counter = 0;

        for (int i = 0; i <= n - 3; i++) {
            int k = INT_MIN;

            if (nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1]) {
                counter++;
                k = nums[i + 1] - nums[i];
            }

            // if an arithmetic slice has been found at index i
            if (k != INT_MIN) {
                int j = 3;

                while (i + j < n) {
                    if (nums[i + j] - nums[i + j - 1] == k) {
                        counter++;
                        j++;
                    } else {
                        break;
                    }
                }
            }
        }

        return counter;
    }
};
