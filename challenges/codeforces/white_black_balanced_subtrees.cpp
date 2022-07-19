/*
 * Solution for 1676/G: White-Black Balanced Subtrees
 *
 * https://codeforces.com/problemset/problem/1676/G
 */
#include <bits/stdc++.h>
using namespace std;

int ans = 0;

int dfs(vector<set<int>>& G, vector<char>& colors, int node) {
    int balance = colors[node] == 'W' ? 1 : -1;

    for (auto child : G[node])
        balance += dfs(G, colors, child);

    if (balance == 0)
        ans++;  // balanced white-black tree

    return balance;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<set<int>> G(n + 1);
        vector<int> parents(n + 1);
        vector<char> colors(n + 1);
        ans = 0;

        for (int i = 2; i <= n; i++)
            cin >> parents[i];

        for (int i = 1; i <= n; i++)
            cin >> colors[i];

        // convert parent notation into adj list graph
        for (int i = n; i >= 0; i--) {
            int node = i;
            while (parents[node] > 0) {
                int par = parents[node];
                G[par].insert(node);
                node = par;
            }
        }

        // dfs tree graph
        dfs(G, colors, 1);
        cout << ans << endl;
    }

    return 0;
}
