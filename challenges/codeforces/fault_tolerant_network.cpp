/*
 * Solution for 1651/C: Fault-Tolerant Network
 *
 * https://codeforces.com/problemset/problem/1651/C
 */
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll INF = 1e17;

vector<int> search_candidates(vector<ll>& choices, ll node) {
    int n = choices.size();
    ll cost = 0;
    ll min_cost = INF;
    vector<int> best = {0, n - 1};  // always try edge nodes as repeated connections can reduce costs

    for (int i = 1; i < n - 1; i++) {
        cost = abs(choices[i] - node);
        if (cost < min_cost)
            min_cost = cost;
    }

    for (int i = 1; i < n - 1; i++) {
        cost = abs(choices[i] - node);
        if (cost == min_cost) {
            best.push_back(i);
            break;
        }
    }

    return best;
}

void solve() {
    int n;
    cin >> n;
    vector<ll> a(n);
    vector<ll> b(n);
    vector<int> choices_a0, choices_an;
    vector<int> choices_b0, choices_bn;

    for (int i = 0; i < n; i++)
        cin >> a[i];
    for (int i = 0; i < n; i++)
        cin >> b[i];

    // search for best candidates to connect edge nodes: a[0], a[n - 1], b[0], b[n - 1]
    choices_a0 = search_candidates(b, a[0]);
    choices_an = search_candidates(b, a[n - 1]);
    choices_b0 = search_candidates(a, b[0]);
    choices_bn = search_candidates(a, b[n - 1]);

    // brute-force all costs with best candidates
    ll min_cost = INF;
    for (int i : choices_a0) {
        for (int j : choices_an) {
            for (int k : choices_b0) {
                for (int q : choices_bn) {
                    ll cost = 0;
                    cost = abs(a[0] - b[i]) + abs(a[n - 1] - b[j]) + abs(b[0] - a[k]) + abs(b[n - 1] - a[q]);

                    // remove duplicated costs for possible duplicated connections between edge nodes
                    if (k == 0 and i == 0)
                        cost -= abs(b[0] - a[0]);

                    if (k == n - 1 and j == 0)
                        cost -= abs(b[0] - a[n - 1]);

                    if (q == 0 and i == n - 1)
                        cost -= abs(b[n - 1] - a[0]);

                    if (q == n - 1 and j == n - 1)
                        cost -= abs(b[n - 1] - a[n - 1]);

                    min_cost = min(min_cost, cost);
                }
            }
        }
    }

    cout << min_cost << endl;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t;
    cin >> t;

    while (t--)
        solve();

    return 0;
}
