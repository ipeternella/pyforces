/*
 * Solution for LC#354: Russian Doll Envelopes
 *
 * https://leetcode.com/problems/russian-doll-envelopes/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        // sort asc and desc to avoid duplicates
        sort(envelopes.begin(), envelopes.end(), sort_order);

        // LIS in O(nlogn) of heights
        return lis_of_heights(envelopes);
    }

    int lis_of_heights(vector<vector<int>>& envelopes) {
        int n = envelopes.size();
        vector<int> tails(n, 0);  // ascending order of final elements of active lis lists
        int lis = 1;

        tails[0] = envelopes[0][1];  // first sequence (lis == 1)
        for (int i = 1; i < n; i++) {
            int h = envelopes[i][1];

            if (h < tails[0]) {
                // case 1: new seq value is smaller than all tails
                tails[0] = h;
            } else if (h > tails[lis - 1]) {
                // case 2: new seq value is bigger than all tails: add it to the end (extend lis)
                tails[lis] = h;
                lis++;
            } else {
                // case 3: new seq value is between [smallest, biggest] so find the first element
                // that's bigger than the new seq value and replace it
                int j = binary_search_ceil(tails, 0, lis - 1, h);
                tails[j] = h;
            }
        }

        return lis;
    }

    // if key is not present: ceil the index to the next element [4, 6] --> return index of 6
    //      i: [0,1,2,3]
    // lis[i]: [1,2,4,6] new key == 5 (between [4,6])
    // binary search ceil returns i == 3 (never i == 2)
    // so lis[i] can be mutated to: [1,2,4,5] which is easier to extend than [1,2,4,6]
    int binary_search_ceil(vector<int>& v, int l, int r, int key) {
        int mid = -1;

        while (l <= r) {
            mid = l + (r - l) / 2;

            if (key > v[mid]) {
                l = mid + 1;
            } else if (key < v[mid]) {
                r = mid - 1;
            } else {
                break;
            }
        }

        return v[mid] < key ? mid + 1 : mid;
    }

    static bool sort_order(vector<int>& env1, vector<int>& env2) {
        int w1 = env1[0], h1 = env1[1];
        int w2 = env2[0], h2 = env2[1];

        if (w1 == w2) {
            return h1 > h2;  // descending in heights for same widths
        }

        return w1 < w2;  // ascending in widths
    }
};
