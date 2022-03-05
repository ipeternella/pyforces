/*
 * Solution for LC#799: Champagne Tower
 *
 * https://leetcode.com/problems/champagne-tower/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        // build an empty champagne tower
        vector<vector<double>> tower;
        for (int i = 0; i <= query_row + 1; i++) {
            vector<double> floor(i + 1, 0.0);
            tower.push_back(floor);
        }

        // fill the tower
        tower[0][0] = poured;
        for (int r = 0; r <= query_row; r++) {
            bool overflowed = false;
            for (int c = 0; c < tower[r].size(); c++) {
                if (tower[r][c] > 1.0) {
                    double excess = (tower[r][c] - 1.0) / 2;
                    overflowed = true;

                    tower[r][c] = 1.0;
                    tower[r + 1][c] += excess;
                    tower[r + 1][c + 1] += excess;
                }
            }

            // nothing has overflowed so no more work to do!
            if (!overflowed)
                break;
        }

        return tower[query_row][query_glass];
    }
};
