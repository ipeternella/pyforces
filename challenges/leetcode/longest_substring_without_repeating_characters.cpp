/*
 * Solution for LC#3: Longest Substring Without Repeating Characters
 *
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> hashmap;
        int n = s.size();
        int len = 0;
        int l = 0;

        // sliding window [l, r] with hashmap to store chars positions
        for (int r = 0; r < n; r++) {
            auto search = hashmap.find(s[r]);

            // stored hashmap index must be greater or equal than l position
            // or is the same as not existing (old index out of current sliding window)
            if (search != hashmap.end() and search->second >= l) {
                int pos = search->second;
                l = pos + 1;
            }

            hashmap[s[r]] = r;          // store char newest position inside current sliding window
            len = max(len, r - l + 1);  // max len
        }

        return len;
    }
};
