/*
 * Solution for 1714/G: Path Prefixes
 *
 * https://codeforces.com/contest/1714/problem/G
 */
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct Edge {
    int a;
    int b;
    int val;
};

void dfs(vector<vector<Edge>>& tree, vector<ll>& r, vector<ll>& prefix_a, vector<ll>& prefix_b, int paren) {
    // binary search (lower bound) to find longest length in which sum B <= A
    if (paren != 1) {
        int i = lower_bound(prefix_b.begin(), prefix_b.end(), prefix_a.back()) - prefix_b.begin();
        int len = min((int)prefix_b.size(), prefix_b[i] <= prefix_a.back() ? i + 1 : i);
        r[paren] = len;
    }

    // return for tree leaves
    if (tree[paren].empty())
        return;

    ll A = prefix_a.empty() ? 0 : prefix_a.back();
    ll B = prefix_b.empty() ? 0 : prefix_b.back();

    for (auto child : tree[paren]) {
        prefix_a.push_back(A + child.a);
        prefix_b.push_back(B + child.b);

        dfs(tree, r, prefix_a, prefix_b, child.val);

        prefix_a.pop_back();
        prefix_b.pop_back();
    }
}

void output_paths() {
    int n;
    cin >> n;
    vector<vector<Edge>> tree(n + 1, vector<Edge>());
    vector<ll> r(n + 1);
    vector<ll> prefix_a;
    vector<ll> prefix_b;

    // create tree with customized edge struct
    for (int node = 2; node <= n; node++) {
        int paren, a, b;
        cin >> paren >> a >> b;
        tree[paren].push_back({a, b, node});
    }

    // dfs to get longest prefix paths
    dfs(tree, r, prefix_a, prefix_b, 1);
    for (int i = 2; i <= n; i++)
        cout << r[i] << " ";
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
        output_paths();

    return 0;
}
