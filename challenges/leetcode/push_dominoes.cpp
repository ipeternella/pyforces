/*
 * Solution for LC#838: Push Dominoes
 *
 * https://leetcode.com/problems/push-dominoes/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string pushDominoes(string dominoes) {
        int n = dominoes.size();
        vector<pair<int, int>> regions;

        // find regions with pushes in opposite directions (R --> <-- L)
        for (int i = 0; i < n; i++) {
            if (dominoes[i] == 'R') {
                int j = i + 1;
                while (j < n and dominoes[j] != 'L') {
                    if (dominoes[j] == 'R')
                        i = j;
                    j++;
                }

                if (j < n) {
                    regions.push_back({i, j});
                    i = j;
                }
            }
        }

        // greedly run pushes all the way left or right
        for (int i = 0; i < n; i++) {
            if (dominoes[i] == 'L') {
                int j = i - 1;
                while (j >= 0 and dominoes[j] == '.') {
                    dominoes[j] = 'L';
                    j--;
                }
            } else if (dominoes[i] == 'R') {
                int j = i + 1;
                while (j < n and dominoes[j] == '.') {
                    dominoes[j] = 'R';
                    j++;
                }
            }
        }

        // correct final simulation by running pushes in opposite directions
        for (auto r : regions)
            push_opposite_forces(dominoes, r.first, r.second);

        return dominoes;
    }

    void push_opposite_forces(string& dominoes, int l, int r) {
        int size = r - l + 1;
        int mid = l + (r - l) / 2;
        if (size & 1) {
            for (int i = l; i < mid; i++)
                dominoes[i] = 'R';
            for (int i = mid + 1; i <= r; i++)
                dominoes[i] = 'L';
            dominoes[mid] = '.';
        } else {
            for (int i = l; i <= mid; i++)
                dominoes[i] = 'R';
            for (int i = mid + 1; i <= r; i++)
                dominoes[i] = 'L';
        }
    }
};
