/*
 * Solution for 1676/F: Longest Strike
 *
 * https://codeforces.com/problemset/problem/1676/F
 */
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9 + 7;

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t;
    cin >> t;

    while (t--) {
        int n, k;
        cin >> n >> k;

        vector<int> A(n + 1);
        for (int i = 0; i < n; i++)
            cin >> A[i];

        A[n] = INF;  // final placeholder to easen the 2 pointer's loop
        sort(A.begin(), A.end());

        int l_ans = -1, r_ans = -1, diff = -1;
        int l = 0, r = 0, f = 0;
        int prev = A[0];

        while (r <= n) {
            if (A[r] == prev) {
                f++;
            } else {
                if (f >= k and A[r - 1] - A[l] >= diff) {
                    l_ans = A[l];
                    r_ans = A[r - 1];
                    diff = A[r - 1] - A[l];
                }

                // if interval is not continuous or freq k is not reached
                // we skip A[r - 1] and start a new range check [l, r]
                if (f < k or A[r] > A[r - 1] + 1) {
                    l = r;
                }

                f = 1;
            }

            prev = A[r];
            r++;
        }

        if (l_ans == -1) {
            cout << -1 << endl;
        } else {
            cout << l_ans << " " << r_ans << endl;
        }
    }

    return 0;
}
