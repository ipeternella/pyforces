/*
 * Solution for LC#61: Rotate List
 *
 * https://leetcode.com/problems/rotate-list/
 */
#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    int size(ListNode* head) {
        ListNode* curr = head;
        int size = 0;

        while (curr) {
            size++;
            curr = curr->next;
        }

        return size;
    }

    ListNode* rotateRight(ListNode* head, int k) {
        if (!head)
            return head;

        int n = size(head);
        k = k % n;

        if (k == 0)
            return head;

        ListNode* curr = head;
        ListNode* old_head = head;
        ListNode* tail;

        for (int i = 0; i < n - 1; i++) {
            if (i == n - k - 1)
                tail = curr;

            curr = curr->next;
        }

        head = tail->next;
        tail->next = nullptr;
        curr->next = old_head;

        return head;
    }
};
