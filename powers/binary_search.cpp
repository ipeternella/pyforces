/*
 * Binary search + lower/upper bounds.
 */
#include <bits/stdc++.h>
using namespace std;

/*
 * Finds the first (lowest) insert position to add an element without
 * breaking ordering.
 *
 * [!]: for values not present in the search space, lower bound == upper bound.
 */
int lower_bound(vector<int>& A, int key, int l, int r) {
    while (l < r) {
        int mid = l + (r - l) / 2;

        if (A[mid] < key) {  // can't be <= or we advance to upper bound
            l = mid + 1;
        } else {
            r = mid;
        }
    }

    // (l + 1) to guarantee num >= key to have right insert index
    // v~~~ if A[l] == 10 (i == 0), return (i + 1) == 2 for key == 20
    // 10 20 20 30
    return A[l] < key ? l + 1 : l;
}

/*
 * Finds the last (highest) insert position to add an element without
 * breaking ordering.
 *
 * [!]: for values not present in the search space, lower bound == upper bound.
 */
int upper_bound(vector<int>& A, int key, int l, int r) {
    while (l < r) {
        int mid = l + (r - l) / 2;

        if (A[mid] <= key) {  // advance to upper bound
            l = mid + 1;
        } else {
            r = mid;
        }
    }

    // (l + 1) to guarantee num > key to have right insert index
    //        v~~~ if A[l] == 20 (i == 2), return i + 1 == 3 for key == 20
    // 10 20 20 30
    return A[l] <= key ? l + 1 : l;
}

/*
 * Traditional binary searching which returns -1 if a key was found in the
 * search space. Returns any position if the search space contains repeated
 * values.
 */
int binary_search(vector<int>& A, int key, int l, int r) {
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (A[mid] == key) {
            return mid;
        } else if (A[mid] <= key) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }

    return -1;
}

void test_upper_bound_should_find_insert_pos() {
    // arrange - value in the array
    vector<int> A = {10, 20, 30, 30, 30, 40, 50};
    int n = A.size();
    int key = 30;

    // act and assert
    assert(upper_bound(A, key, 0, n - 1) == 5);

    // arrange - value beyond the max value
    key = 55;

    // act and assert
    assert(upper_bound(A, key, 0, n - 1) == 7);

    // arrange
    key = 10;

    // act and assert
    assert(upper_bound(A, key, 0, n - 1) == 1);

    // arrange - value below the min value
    key = 2;

    // act and assert
    assert(upper_bound(A, key, 0, n - 1) == 0);
}

void test_lower_bound_should_find_insert_pos() {
    // arrange - value in the array
    vector<int> A = {10, 20, 30, 30, 30, 40, 50};
    int n = A.size();
    int key = 30;

    // act and assert
    assert(lower_bound(A, key, 0, n - 1) == 2);

    // arrange - value beyond max value
    key = 55;

    // act and assert
    assert(lower_bound(A, key, 0, n - 1) == 7);

    // arrange - value beyond max value
    key = 10;

    // act and assert
    assert(lower_bound(A, key, 0, n - 1) == 0);

    // arrange - value below min value
    key = 5;

    // act and assert
    assert(lower_bound(A, key, 0, n - 1) == 0);
}

void test_binary_search_should_not_find_key() {
    // arrange
    vector<int> A = {10, 20, 30, 40, 50};
    int n = A.size();
    int key = 25;

    // act and assert
    assert(binary_search(A, key, 0, n - 1) == -1);
}

void test_binary_search_should_find_key() {
    // arrange
    vector<int> A = {10, 20, 30, 40, 50};
    int n = A.size();
    int key = 30;

    // act and assert
    assert(binary_search(A, key, 0, n - 1) == 2);
}

int main() {
    // traditional bs
    test_binary_search_should_not_find_key();
    test_binary_search_should_find_key();

    // lower bound for search spaces with repeated values
    test_lower_bound_should_find_insert_pos();

    // upper bound
    test_upper_bound_should_find_insert_pos();

    return 0;
}
