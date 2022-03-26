/*
 * Solution for LC#881: Boats to Save People
 *
 * https://leetcode.com/problems/boats-to-save-people/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        set<int> picked;
        int n = people.size();
        int last_r = n - 1;
        int l = 0;
        int boats = 0;

        // greedy: pick people with as less weight as possible with
        // as much weight as possible!
        sort(people.begin(), people.end());
        for (int i = 0; i < n; i++) {
            int r = last_r;
            l = i;

            while (l < r) {
                if (people[l] + people[r] <= limit) {
                    last_r = r - 1;
                    picked.insert(r);
                    boats++;
                    break;
                } else {
                    r--;
                }
            }

            if (l >= r)
                break;  // from l (inclusive) and onwards: boats with people alone: can't have a pair!
        }

        for (int i = l; i < n; i++) {
            if (picked.find(i) == picked.end())
                boats++;
        }

        return boats;
    }
};
