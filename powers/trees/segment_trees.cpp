/*
 * Algorithms that use segment trees whose statistical function is the sum of segments. Segment trees
 * can be used to represent segments of ints, chars, structures, etc.
 */
#include <bits/stdc++.h>
using namespace std;

struct segment_tree {
    int n;
    vector<int> st;

    segment_tree(vector<int>& v) {
        n = v.size();
        st.resize(4 * n);  // fill remaining space with zeros if necessary
        build(0, n - 1, 0, v);
    }

    // i -> index that translates range from v to st[i] node
    void build(int v_left, int v_right, int i, vector<int>& v) {
        if (v_left == v_right) {
            st[i] = v[v_left];
            return;
        }
        int v_mid = (v_left + v_right) / 2;

        // st_left = 2*i + 1, st_right = 2*i + 2
        // every new v slice goes ~ 2*i further in st!
        build(v_left, v_mid, 2 * i + 1, v);
        build(v_mid + 1, v_right, 2 * i + 2, v);
        st[i] = st[2 * i + 1] + st[2 * i + 2];
    }

    int query(int left, int right) {
        return query(0, n - 1, left, right, 0);
    }

    int query(int v_left, int v_right, int left, int right, int i) {
        // no overlapping: vector range is completely outside of target range: [v_right < left, right < v_left]
        if (v_left > right or v_right < left)
            return 0;

        // complete overlap: vector range is inside target range: [v_left >= left, v_right <= right]
        if (v_left >= left and v_right <= right)
            return st[i];

        // partial overlap: vector range partially overlaps target range
        int v_mid = (v_left + v_right) / 2;
        int l_query = query(v_left, v_mid, left, right, 2 * i + 1);
        int r_query = query(v_mid + 1, v_right, left, right, 2 * i + 2);

        return l_query + r_query;
    }

    void update(int v_index, int value) {
        // v_index -> index to update with new value
        update(0, n - 1, v_index, value, 0);
    }

    void update(int v_left, int v_right, int v_index, int value, int i) {
        if (v_left == v_right) {
            st[i] = value;
            return;
        }

        int v_mid = (v_left + v_right) / 2;

        if (v_index <= v_mid) {
            update(v_left, v_mid, v_index, value, 2 * i + 1);
        } else {
            update(v_mid + 1, v_right, v_index, value, 2 * i + 2);
        }

        // update current node with children sum
        st[i] = st[2 * i + 1] + st[2 * i + 2];
    }
};

int main() {
    vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8};
    segment_tree tree(v);  // tree whose statistical fn = sum of segments

    cout << tree.query(0, 4) << endl;
    cout << tree.query(2, 6) << endl;

    tree.update(4, 10);

    cout << tree.query(0, 4) << endl;
    cout << tree.query(2, 6) << endl;
}
