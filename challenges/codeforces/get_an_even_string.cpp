/*
 * Solution for 1660/C: Get An Even String
 *
 * https://codeforces.com/problemset/problem/1660/C
 */
#include <bits/stdc++.h>
using namespace std;

int delete_chars(vector<int>& f) {
    int remove = 0;
    for (int k = 0; k < 26; k++) {
        if (f[k] > 0) {
            f[k] = 0;
            remove++;
        }
    }

    return remove;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t;
    cin >> t;

    while (t--) {
        string s;
        cin >> s;
        vector<int> f(26);
        int n = s.size();
        int remove = 0;

        for (int i = 0; i < n; i++) {
            int j = s[i] - 'a';
            if (f[j] == 0) {
                f[j]++;  // candidate to be removed
            } else {
                f[j] = 0;  // has a pair: remove previous candidates
                remove += delete_chars(f);
            }
        }

        remove += delete_chars(f);
        cout << remove << endl;
    }

    return 0;
}
