/*
 * Solution for LC#21: Merge Two Sorted Lists
 *
 * https://leetcode.com/problems/merge-two-sorted-lists/
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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *head = nullptr, *curr = nullptr;

        while (list1 and list2) {
            if (list1->val <= list2->val) {
                if (!head) {
                    head = list1;
                    curr = head;
                } else {
                    curr->next = list1;
                    curr = curr->next;
                }
                list1 = list1->next;
            } else {
                if (!head) {
                    head = list2;
                    curr = head;
                } else {
                    curr->next = list2;
                    curr = curr->next;
                }
                list2 = list2->next;
            }
        }

        // append the remaining list (if any) or if one of the lists were empty
        if (head)
            curr->next = list1 ? list1 : list2;
        else
            head = list1 ? list1 : list2;

        return head;
    }
}
