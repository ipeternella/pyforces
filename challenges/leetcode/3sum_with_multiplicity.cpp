/*
 * Solution for LC#923: 3Sum With Multiplicity
 *
 * https://leetcode.com/problems/3sum-with-multiplicity/
 */
#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define P 1000000007

class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        int n = arr.size();
        ll total = 0;

        for (int i = 0; i <= n - 3; i++) {
            int target_2sum = target - arr[i];
            vector<int> freqs(101, 0);

            // build hashmap of frequencies of the remaining elements
            for (int j = i + 1; j < n; j++) {
                freqs[arr[j]]++;
            }

            // reduce 2sum problem
            for (int j = i + 1; j < n; j++) {
                int required = target_2sum - arr[j];
                freqs[arr[j]]--;

                if (required <= 100 and required >= 0 and freqs[required] > 0) {
                    total = (total + freqs[required]) % P;
                }
            }
        }

        return total;
    }
};
