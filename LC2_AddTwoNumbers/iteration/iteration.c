/* You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
* You may assume the two numbers do not contain any leading zero, except the number 0 itself.
*/

/* Input: l1 = [2,4,3], l2 = [5,6,4]
* Output: [7,0,8]
* Explanation: 342 + 465 = 807.
* Input: l1 = [0], l2 = [0]
* Output: [0]
* Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
* Output: [8,9,9,9,0,0,0,1]
*/

/* iteration
* Time Complexity: O(max(len(l1),len(l2)))
* Space Complexity: O(max(len(l1),len(l2)))
*/

# include <stdio.h>
# include <stdlib.h>
struct ListNode{
    int val;
    struct ListNode *next;
};

struct ListNode* newListNode(int val){
    struct ListNode* newNode = malloc(sizeof(struct ListNode));
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    int total = 0;
    int isNextOne = 0;
    struct ListNode* result = malloc(sizeof(struct ListNode));
    result->next = NULL;
    struct ListNode* curr = result;
    struct ListNode* l1Curr = l1;
    struct ListNode* l2Curr = l2;

    while(l1Curr != NULL && l2Curr != NULL){
        total = l1Curr->val + l2Curr->val + isNextOne;
        isNextOne = total / 10;
        curr->next = newListNode(total % 10);
        curr = curr->next;
        l1Curr = l1Curr->next;
        l2Curr = l2Curr->next;
    }

    while(l1Curr != NULL){
        total = l1Curr->val + isNextOne;
        isNextOne = total / 10;
        curr->next = newListNode(total % 10);
        curr = curr->next;
        l1Curr = l1Curr->next;
    }

    while(l2Curr != NULL){
        total = l2Curr->val + isNextOne;
        isNextOne = total / 10;
        curr->next = newListNode(total % 10);
        curr = curr->next;
        l2Curr = l2Curr->next;
    }

    if(isNextOne != 0){
        curr->next = newListNode(isNextOne);
    }

    struct ListNode* temp = result;
    result = result->next;
    free(temp);

    return result;
    
}


int main(){
    struct ListNode* l1 = newListNode(2);
    l1->next =  newListNode(4);
    l1->next->next =  newListNode(3);

    struct ListNode* l2 =  newListNode(5);
    l2->next =  newListNode(6);
    l2->next->next =  newListNode(4);

    struct ListNode* result = addTwoNumbers(l1, l2);
    while(result != NULL){
        printf("%d\n", result->val);
        result = result->next;
    }
}