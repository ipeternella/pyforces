/*
 * Solution for LC#1721: Swapping Nodes in a Linked List
 *
 * https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
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
    ListNode* swapNodes(ListNode* head, int k) {
        int n = size(head);
        auto start = get_node(head, k);
        auto end = get_node(head, n - k + 1);  // n - k - 1 (count from end to the beginning)

        if (n < 2)
            return head;

        // start becomes the end if k > n / 2
        if (n - k + 1 < k) {
            auto tmp = start;
            start = end;
            end = tmp;
        }

        ListNode* start_prev = start.second;
        ListNode* start_node = start.first;
        ListNode* end_prev = end.second;
        ListNode* end_node = end.first;
        ListNode* end_next = end_node->next;

        // special cases: k == 1 or k == n AND/OR adjacent nodes to swap
        if (k == 1 or k == n) {
            if (start_node->next == end_node) {  // adj nodes
                head = end.first;
                end_node->next = start_node;
                start_node->next = nullptr;
            } else {
                end.first->next = head->next;
                head->next = nullptr;
                head = end.first;
                end_prev->next = start.first;
            }
        } else {
            start_prev->next = end_node;

            // adj nodes
            if (start_node->next == end_node) {
                end_node->next = start_node;
            } else {
                end_node->next = start_node->next;
            }

            end_prev->next = start_node;
            start_node->next = end_next;
        }

        return head;
    }

    // helper functions
    int size(ListNode* head) {
        ListNode* curr = head;
        int size = 0;

        while (curr) {
            size++;
            curr = curr->next;
        }

        return size;
    }

    pair<ListNode*, ListNode*> get_node(ListNode* head, int pos) {
        ListNode* curr = head;
        ListNode* prev = nullptr;
        int i = 1;

        while (curr and i < pos) {
            i++;
            prev = curr;
            curr = curr->next;
        }

        return make_pair(curr, prev);
    }
};
