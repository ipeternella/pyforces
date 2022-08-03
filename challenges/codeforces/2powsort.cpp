/*
 * Solution for 1692/G: 2^Sort
 *
 * https://codeforces.com/problemset/problem/1692/G
 */
#include <bits/stdc++.h>
#define ll long long
using namespace std;

void count_2powsort() {
    int n, K;
    cin >> n >> K;
    vector<ll> a(n);

    for (int i = 0; i < n; i++)
        cin >> a[i];

    int len = 1;        // len of subarrays 2pow sorted
    int subarrays = 0;  // count of subarrays 2pow sorted
    for (int i = 1; i < n; i++) {
        if (2 * a[i] <= a[i - 1]) {
            len = 1;
        } else {
            len++;
            if (len >= K + 1) {
                subarrays++;
            }
        }
    }

    cout << subarrays << endl;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int t;
    cin >> t;

    while (t--)
        count_2powsort();

    return 0;
}
