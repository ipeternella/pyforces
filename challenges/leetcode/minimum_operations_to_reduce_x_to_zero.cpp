/*
 * Solution for LC#1658: Minimum Operations to Reduce X to Zero
 *
 * https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    const int NOT_FOUND = 1e9 + 7;

    // O(nlogn) time and O(n) space solution with binary searching + prefix sums
    int minOperations(vector<int>& nums, int x) {
        vector<int> prefixes;
        vector<int> suffixes;
        int n = nums.size();
        int pref_s = 0, suf_s = 0;
        int ops = NOT_FOUND;

        for (int i = 0; i < n; i++) {
            pref_s += nums[i];
            suf_s += nums[n - 1 - i];

            prefixes.push_back(pref_s);
            suffixes.push_back(suf_s);
        }

        int j = binary_search(suffixes, 0, n - 1, x);
        int k = binary_search(prefixes, 0, n - 1, x);

        if (j != NOT_FOUND)
            ops = j + 1;

        if (k != NOT_FOUND)
            ops = min(ops, k + 1);

        // O(n*logn) algorithm
        for (int i = 0; i < n - 1; i++) {
            pref_s = prefixes[i];
            int j = binary_search(suffixes, 0, n - 2 - i, x - pref_s);

            if (j != NOT_FOUND)
                ops = min(ops, (i + 1) + (j + 1));
        }

        return ops != NOT_FOUND ? ops : -1;
    }

    int binary_search(vector<int>& nums, int l, int r, int key) {
        while (l <= r) {
            int mid = l + (r - l) / 2;

            if (nums[mid] == key) {
                return mid;
            } else if (nums[mid] > key) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return NOT_FOUND;
    }

    // O(n) time and O(1) space solution with 2-pointers
    int minOperationsII(vector<int>& nums, int x) {
        int n = nums.size();
        int l = n - 1, r = n;
        int ops = NOT_FOUND;
        int sum = 0;

        for (int i = 0; i < n; i++)
            sum += nums[i];

        // impossible to reach x even with all values
        if (sum < x)
            return -1;

        while (l >= -1 and r >= 0) {
            if (sum > x) {
                // nothing else to remove as l == -1
                if (l == -1)
                    break;
                sum -= nums[l--];
            } else if (sum < x) {
                sum += nums[--r];
            } else {
                ops = min(ops, (l + 1) + (n - r));

                if (l >= 0)
                    sum -= nums[l--];
                else
                    break;
            }
        }

        return ops != NOT_FOUND ? ops : -1;
    }
};
