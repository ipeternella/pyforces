/*
 * Solution for LC#1647: Minimum Deletions to Make Character Frequencies Unique
 *
 * https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDeletions(string s) {
        vector<int> f(26, 0);  // freqs of 26 possible lowercase English letters (~ int hashmap)
        int n = s.size();
        int changes = 0;

        for (int i = 0; i < n; i++) {
            int char_i = s[i] - 'a';
            f[char_i] += 1;  // freq for each char
        }

        // start from bigger frequencies and move to lower ones removing duplicates as required
        sort(f.begin(), f.end(), greater<int>());
        for (int i = 1; i < 26; i++) {
            if (f[i] == 0)
                break;

            if (f[i] == f[i - 1]) {
                // delete char and reduce its freq by 1 to remove duplicated frequencies
                // and update f[i] to f[i] - 1 because this new lower freq can also be duplicated
                changes++;
                f[i]--;
            } else if (f[i] > f[i - 1]) {
                // if f[i] > f[i - 1] means that f[i - 1] had chars removed so f[i]
                // must have the same amount of chars removed + 1 (unless f[i - 1] is zero already)
                int diff = f[i - 1] == 0 ? f[i] : f[i] - f[i - 1] + 1;
                f[i] = max(0, f[i - 1] - 1);

                changes += diff;
            }
        }

        return changes;
    }
};
