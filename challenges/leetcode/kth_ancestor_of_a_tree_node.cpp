/*
 * Solution for LC#1483: Kth Ancestor of a Tree Node
 *
 * https://leetcode.com/problems/kth-ancestor-of-a-tree-node/
 */
#include <bits/stdc++.h>
using namespace std;

class TreeAncestor {
    // making q queries on an n-node tree: O(q*n) ~ O(n^2) which is NOT acceptable for n ~ 5 * 10^4
    vector<vector<int>> ancestors;  // pre-processing with binary-lifting for O(q*logn) ~ O(nlogn)
    vector<int> height;
    int POW2_MAX = 20;

public:
    TreeAncestor(int n, vector<int>& parent) {
        ancestors = vector<vector<int>>(n, vector<int>(POW2_MAX));
        height = vector<int>(n);
        parent[0] = 0;  // avoid undef behavior with -1 all ancestors that do not exist now endup at root 0

        // set all parents first as the nodes parents may not follow: parent[i] < i
        for (int node = 0; node < n; node++) {
            ancestors[node][0] = parent[node];
        }

        // binary lifting: p = 1 means 2^1 = 2nd parent, p = 2 means 2^2 = 4th parent, etc.
        for (int p = 1; p < POW2_MAX; p++) {
            for (int node = 0; node < n; node++) {
                if (node > 0)
                    height[node] = height[parent[node]] + 1;

                ancestors[node][p] = ancestors[ancestors[node][p - 1]][p - 1];
            }
        }
    }

    int getKthAncestor(int node, int k) {
        int p = 0;
        int ancestor = node;

        if (height[node] < k)
            return -1;

        // fetch parents of parents in powers of 2: binary lifting
        while (k) {
            if (k & 1)
                ancestor = ancestors[ancestor][p];
            p++;
            k >>= 1;
        }

        return ancestor;
    }
};
