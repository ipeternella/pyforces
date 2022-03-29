/*
 * Solution for LC#763: Partition Labels
 *
 * https://leetcode.com/problems/partition-labels/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> partitionLabels(string s) {
        int n = s.size();
        vector<int> map(26, 0);         // map of last positions of each char
        vector<int> partitions = {-1};  // partitions indexes
        vector<int> sizes;

        for (int i = 0; i < n; i++) {
            int k = s[i] - 'a';  // relative index for each char from 0 (a).. 25 (z)
            map[k] = max(map[k], i);
        }

        int last_pos = map[s[0] - 'a'];
        for (int i = 0; i < n; i++) {
            int k = s[i] - 'a';
            int new_last_pos = map[k];

            // every time the current index is bigger than the last position: new partition
            if (i > last_pos)
                partitions.push_back(i - 1);

            last_pos = max(last_pos, new_last_pos);
        }

        // build partitions sizes based on the partitions indexes
        partitions.push_back(n - 1);
        for (int i = 1; i < partitions.size(); i++)
            sizes.push_back(partitions[i] - partitions[i - 1]);

        return sizes;
    }
};
