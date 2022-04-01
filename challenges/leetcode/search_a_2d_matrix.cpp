/*
 * Solution for LC#74: Search a 2D Matrix
 *
 * https://leetcode.com/problems/search-a-2d-matrix/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int binary_search_row(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int s = 0;
        int e = m - 1;
        int mid = (s + e) / 2;

        while (s <= e) {
            mid = (s + e) / 2;

            if (matrix[mid][0] > target) {
                e = mid - 1;
            } else if (matrix[mid][0] < target) {
                s = mid + 1;
            } else {
                return mid;
            }
        }

        mid = matrix[mid][0] > target ? mid - 1 : mid;
        return max(0, mid);  // can't be below 0
    }

    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix[0].size();
        int l = 0;
        int r = n - 1;
        int row = binary_search_row(matrix, target);  // search for row first

        while (l <= r) {
            int mid = (l + r) / 2;

            if (matrix[row][mid] > target) {
                r = mid - 1;
            } else if (matrix[row][mid] < target) {
                l = mid + 1;
            } else {
                return true;
            }
        }

        return false;
    }
};
