/*
 * Solution for 1741/D: Masha and a Beautiful Tree
 *
 * https://codeforces.com/problemset/problem/1741/D
 */
#include <bits/stdc++.h>
using namespace std;

void swap_range(vector<int>& a, int s1, int e1, int s2, int e2) {
    if (s1 == e1) {
        swap(a[s1], a[s2]);
        return;
    }

    vector<int> tmp;
    int k = s1;
    for (int i = s2; i <= e2; i++) {
        tmp.push_back(a[i]);
        a[i] = a[k++];
    }
    k = 0;
    for (int i = s1; i <= e1; i++) {
        a[i] = tmp[k++];
    }
}

int solve() {
    int m;
    cin >> m;

    vector<int> leaves(m);
    for (int i = 0; i < m; i++) {
        cin >> leaves[i];
    }

    int swaps = 0;
    for (int p = 1; p <= m / 2; p *= 2) {
        for (int i = 0; i < m; i += 2 * p) {
            if (leaves[i] > leaves[i + p]) {
                swap_range(leaves, i, i + p - 1, i + p, i + 2 * p - 1);
                swaps++;
            }
        }
    }

    for (int i = 0; i < m - 1; i++)
        if (leaves[i] > leaves[i + 1])
            return -1;

    return swaps;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t;
    cin >> t;

    while (t--)
        cout << solve() << endl;

    return 0;
}
