/*
 * Solution for LC#1337: The K Weakest Rows in a Matrix
 *
 * https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int m = mat.size();
        int n = mat[0].size();
        vector<int> soldiers;

        // O(m*n)
        for (int r = 0; r < m; r++) {
            bool all_ones = true;
            for (int c = 0; c < n; c++) {
                if (mat[r][c] == 0) {
                    soldiers.push_back(c);
                    all_ones = false;
                    break;
                }
            }
            if (all_ones)
                soldiers.push_back(n);
        }

        // O(m*n) -> acceptable for n, m <= 100
        vector<int> k_weakest;
        for (int s = 0; s <= n; s++) {
            for (int j = 0; j < m; j++) {
                if (soldiers[j] == s)
                    k_weakest.push_back(j);

                if (k_weakest.size() == k)
                    return k_weakest;
            }
        }

        return k_weakest;
    }
};
