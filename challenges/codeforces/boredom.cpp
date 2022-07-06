/*
 * Solution for: 455/A. Boredom
 *
 * https://codeforces.com/problemset/problem/455/A
 */
#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int N = 100005;

ll play(vector<ll>& u, vector<ll>& f, vector<ll>& dp, int i) {
    int n = u.size();
    if (i >= n)
        return 0;

    if (dp[i] != -1)
        return dp[i];

    ll take = 0;
    if (i + 1 < n and u[i + 1] == u[i] + 1) {
        take = play(u, f, dp, i + 2) + f[u[i]] * u[i];
    } else {
        take = play(u, f, dp, i + 1) + f[u[i]] * u[i];
    }

    ll dont_take = play(u, f, dp, i + 1);
    return dp[i] = max(take, dont_take);
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int n;
    cin >> n;

    ll num;
    vector<ll> u;
    vector<ll> dp(n + 1, -1);
    vector<ll> f(N);

    for (int i = 0; i < n; i++) {
        cin >> num;

        if (f[num] == 0)
            u.push_back(num);

        f[num]++;
    }

    sort(u.begin(), u.end());
    cout << play(u, f, dp, 0) << endl;

    return 0;
}
