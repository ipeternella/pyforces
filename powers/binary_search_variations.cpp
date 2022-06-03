/*
 * Some studies about some variations of Binary Search. Some might include final search
 * spaces that are a range. Some might find lower and upper boundaries (keep searching after
 * the key as been found), etc.
 */
#include <bits/stdc++.h>
using namespace std;

void print_vector(vector<int>& nums) {
    int n = nums.size();

    cout << "vector:" << endl;

    cout << "  i:  ";
    for (int i = 0; i < n; i++) {
        cout << i << " ";
    }
    cout << endl;

    cout << "a[i]: ";
    for (auto num : nums) {
        cout << num << " ";
    }

    cout << endl;
}

void print_search_space(int l, int r, int mid) {
    cout << "[l, r]: "
         << "[" << l << ", " << r << "]"
         << ", mid: " << mid << endl;
}

int binary_search_range(vector<int>& nums, int key, bool ceil = true) {
    int l = -1;  // keeps [l, r] at least one unit away to aways keep [floor, ceil] search space
    int r = nums.size() - 1;
    print_search_space(l, r, -1);

    // keeps reducing search space until [l, r] are just one unit away which means
    // the final search space has just two possible values: [l, r] == [l, l + 1] == [floor, ceil]
    while (r - l > 1) {  // controls final search space size: r == l + 1 breaks the loop
        int mid = l + (r - l) / 2;

        if (key > nums[mid]) {
            l = mid;
            print_search_space(l, r, mid);
        } else {
            r = mid;
            print_search_space(l, r, mid);
        }
    }

    return ceil ? r : l;
}

int binary_search(vector<int>& nums, int key) {
    int l = 0;
    int r = nums.size() - 1;
    print_search_space(l, r, -1);

    // returns when key is found or when left bounary exceeds right one which
    // means search space has been completely exhausted and not reduced
    // to a range [l, r] as it's done in binary_search_range
    while (l <= r) {
        int mid = l + (r - l) / 2;

        if (nums[mid] == key) {
            cout << "key hit!" << endl;
            return mid;
        } else if (key > nums[mid]) {
            l = mid + 1;
            print_search_space(l, r, -1);
        } else {
            r = mid - 1;
            print_search_space(l, r, -1);
        }
    }

    return -1;
}

int main() {
#ifdef LOCAL_ONLY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int n, key;
    vector<int> nums;

    cin >> n >> key;
    while (n--) {
        int num;
        cin >> num;
        nums.push_back(num);
    }

    n = nums.size();
    sort(nums.begin(), nums.end());

    cout << "search key: " << key << endl;
    print_vector(nums);

    cout << endl << "bs - traditional:" << endl;
    cout << binary_search(nums, key) << endl;

    cout << endl << "bs - search space of 2 units:" << endl;
    cout << binary_search_range(nums, key, false) << endl;

    cout << endl << "bs - search space of 2 units:" << endl;
    cout << binary_search_range(nums, key) << endl;

    return 0;
}
