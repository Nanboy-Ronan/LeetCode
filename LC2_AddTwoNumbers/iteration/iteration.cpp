/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

#include <iostream>
using namespace std;

class Solution {
public:
    struct ListNode {
        int val;
        ListNode *next;
        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode *next) : val(x), next(next) {}
    };

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Iteration
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        if(l1 == nullptr && l2 == nullptr){
            return nullptr;
        }
        if(l1 == nullptr){
            return l1;
        }
        if(l2 == nullptr){
            return l2;
        }

        ListNode* result = new ListNode();
        ListNode* pointer = result;
        // l1 = l1->next;
        // l2 = l2->next;

        int next = 0;
        // if(l1->val + l2->val)
        while(l1 != nullptr && l2 != nullptr){
            int added = l1->val + l2->val + next;
            int nodeVal;

            if(next != 0){
                next = 0;
            }

            if(added >= 10){
                nodeVal = added % 10;
                next = 1;
            }else {
                nodeVal = added;
            }

            ListNode* temp = new ListNode(nodeVal);
            pointer->next = temp;
            pointer = pointer->next;

            l1 = l1->next;
            l2 = l2->next;
        }

        while(l1 != nullptr){
            int added = l1->val + next;
            int nodeVal;
            
            if(next != 0){
                next = 0;
            }
            if(added >= 10){
                nodeVal = added % 10;
                next = 1;
            }else {
                nodeVal = added;
            }

            ListNode* temp = new ListNode(nodeVal);
            pointer->next = temp;
            pointer = pointer->next;

            l1 = l1->next;
        }

        while(l2 != nullptr){
            int added = l2->val + next;
            int nodeVal;
            
            if(next != 0){
                next = 0;
            }
            if(added >= 10){
                nodeVal = added % 10;
                next = 1;
            }else {
                nodeVal = added;
            }

            ListNode* temp = new ListNode(nodeVal);
            pointer->next = temp;
            pointer = pointer->next;

            l2 = l2->next;
        }

        if(next != 0){
            ListNode* temp = new ListNode(next);
            pointer->next = temp;
        }

        return result->next;
    }
};