/*
 * Solution for 1553/D: Backspace
 *
 * https://codeforces.com/problemset/problem/1553/D
 */
#include <bits/stdc++.h>
using namespace std;

void solve() {
    string s, t;
    cin >> s >> t;
    int n = s.size();
    int m = t.size();

    if (m > n) {
        cout << "NO" << endl;
        return;
    }

    int i = n - 1;
    int j = m - 1;
    while (i >= 0) {
        if (j >= 0 and s[i] == t[j]) {
            i--;
            j--;
        } else {
            i -= 2;
        }

        // j >= 0, but i < 0: nothing more to do: impossible, so break
        // j < 0 and i < 0: goal!
        // j < 0, but i >= 0: still have chars to remove, but we can always remove the rest: goal!
        if ((j < 0 and i < 0) or (j < 0 and i >= 0)) {
            cout << "YES" << endl;
            return;
        }
    }

    cout << "NO" << endl;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int q;
    cin >> q;

    while (q--)
        solve();

    return 0;
}
