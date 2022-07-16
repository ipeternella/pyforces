/*
 * Solution for 1669/G: Fall Down
 *
 * https://codeforces.com/problemset/problem/1669/G
 */
#include <bits/stdc++.h>
using namespace std;

void print_grid(vector<vector<char>>& grid) {
    int n = grid.size();
    int m = grid[0].size();

    for (int r = 0; r < n; r++) {
        for (int c = 0; c < m; c++) {
            cout << grid[r][c];
        }
        cout << endl;
    }
}

void simulate(vector<vector<char>>& grid) {
    int n = grid.size();
    int m = grid[0].size();

    for (int r = n - 2; r >= 0; r--) {
        for (int c = 0; c < m; c++) {
            if (grid[r][c] == '*') {
                for (int r2 = r + 1; r2 < n; r2++) {
                    if (grid[r2][c] == '.' and r2 == n - 1) {
                        grid[r][c] = '.';
                        grid[r2][c] = '*';
                        break;
                    } else if (grid[r2][c] != '.') {
                        grid[r][c] = '.';
                        grid[r2 - 1][c] = '*';
                        break;
                    }
                }
            }
        }
    }
    print_grid(grid);
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<vector<char>> grid(n, vector<char>(m, '.'));

        for (int r = 0; r < n; r++)
            for (int c = 0; c < m; c++)
                cin >> grid[r][c];

        simulate(grid);
    }

    return 0;
}
