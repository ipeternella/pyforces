/*
 * Solution for 1706/C: Qpwoeirut And The City
 *
 * https://codeforces.com/problemset/problem/1706/C
 */
#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll build_peak(vector<ll>& h, int i) {
    ll diff = h[i] - max(h[i - 1], h[i + 1]);
    ll extra = 0;
    if (diff <= 0)
        extra += abs(diff) + 1;

    return extra;
}

ll architect(vector<ll>& h) {
    int n = h.size();
    ll floors = 0;

    // even buildings -> just one possible config to maximize cool buildings
    // ex: 01010
    if (n % 2 != 0) {
        for (int i = 1; i < n; i += 2)
            floors += build_peak(h, i);

        return floors;
    }

    // odd buildings -> many configs to maximize: pick one with min floors
    // ex: 001010, 010010, 010100 (sliding window of 2 adjacent non-cool buildings)
    ll f = 0;
    for (int i = 2; i < n; i += 2)
        f += build_peak(h, i);

    // reuse first configuration solution with a sliding window of non-cool buildings
    // to capture the min amount of floors possible
    floors = f;
    for (int i = 2; i < n; i += 2) {
        int j = i - 1;

        f -= build_peak(h, i);
        f += build_peak(h, j);
        floors = min(floors, f);
    }

    return floors;
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

        vector<ll> h(n);
        for (int i = 0; i < n; i++)
            cin >> h[i];

        cout << architect(h) << endl;
    }

    return 0;
}
