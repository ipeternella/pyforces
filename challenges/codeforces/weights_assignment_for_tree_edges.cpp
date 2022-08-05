/*
 * Solution for 1611/D: Weights Assignment For Tree Edges
 *
 * https://codeforces.com/problemset/problem/1611/D
 */
#include <bits/stdc++.h>
using namespace std;

void assign_tree_wts() {
    int n, root;
    cin >> n;
    vector<int> b(n + 1);
    vector<int> w(n + 1);
    vector<int> d(n + 1);
    vector<int> p(n + 1);

    for (int i = 1; i <= n; i++) {
        cin >> b[i];
        if (i == b[i])
            root = i;
    }

    for (int i = 1; i <= n; i++)
        cin >> p[i];

    // assign distances according to permutation's p[i] order
    int k = 0;
    for (int i = 1; i <= n; i++) {
        d[p[i]] = k++;
    }

    // sanity check if p[i] is viable: d[b[i]] < d[i] (dist parent < dist child, except root)
    for (int i = 1; i <= n; i++) {
        if (d[b[i]] >= d[i] and i != root) {
            cout << "-1" << endl;
            return;
        }
        w[i] = d[i] - d[b[i]];  // weights according to tree's edges (diff between parent and child)
    }

    for (int i = 1; i <= n; i++)
        cout << w[i] << " ";

    cout << endl;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int t;
    cin >> t;

    while (t--)
        assign_tree_wts();

    return 0;
}
