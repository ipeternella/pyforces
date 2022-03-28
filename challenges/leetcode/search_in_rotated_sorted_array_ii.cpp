/*
 * Solution for LC#81: Search in Rotated Sorted Array II
 *
 * https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool binary_search(vector<int>& nums, int start, int end, int target) {
        int l = start;
        int r = end;

        while (l <= r) {
            int mid = (l + r) / 2;
            if (nums[mid] > target) {
                r = mid - 1;
            } else if (nums[mid] < target) {
                l = mid + 1;
            } else {
                return true;
            }
        }

        return false;
    }

    bool search(vector<int>& nums, int target) {
        int n = nums.size();
        int pivot = -1;
        int prev = nums[0];

        // find pivot of the rotation
        for (int i = 1; i < n; i++) {
            int curr = nums[i];

            if (curr < prev) {
                pivot = i - 1;
                break;
            }

            prev = curr;
        }

        // if there's a pivot: binary search in both partitions of the array
        if (pivot != -1) {
            if (binary_search(nums, 0, pivot, target))
                return true;

            return binary_search(nums, pivot + 1, n - 1, target);
        }

        // if there's no pivot (full rotation): simple binary search
        return binary_search(nums, 0, n - 1, target);
    }
};
