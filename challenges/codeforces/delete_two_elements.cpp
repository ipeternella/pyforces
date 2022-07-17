/*
 * Solution for 1598/C: Delete Two Elements
 *
 * https://codeforces.com/problemset/problem/1598/C
 */
#include <bits/stdc++.h>
#define int long long
using namespace std;

int32_t main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t;
    cin >> t;

    while (t--) {
        int n;
        int sum = 0;
        int pairs = 0;
        cin >> n;
        vector<int> A(n);
        unordered_map<int, int> F;  // hashtable of frequencies
        F.reserve(n);               // avoid rehashes: reserve bucket_size for at least n keys

        for (int i = 0; i < n; i++) {
            cin >> A[i];
            sum += A[i];
            auto search = F.find(A[i] * n);

            // use A[i] * n to avoid divisions by n (avoid using doubles)
            if (search == F.end()) {
                F[A[i] * n] = 1;
            } else {
                F[A[i] * n]++;
            }
        }

        // check if required pair value of A[i] * n exists (freq > 0)
        for (int i = 0; i < n; i++) {
            F[A[i] * n]--;  // update freq table: check for targets ahead of A[i]

            int target = 2 * sum - A[i] * n;  // required value for A[i] * n (other pair element)
            auto search = F.find(target);

            if (search != F.end())
                pairs += F[target];
        }

        cout << pairs << endl;
    }

    return 0;
}
