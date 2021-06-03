# Given the head of a singly linked list, return true if it is a palindrome.
# Input: head = [1,2,2,1]
# Output: true
# Input: head = [1,2]
# Output: false

from typing import List


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    # recursion
    # Time Complexity: O(n)
    # Space COmplexity： O(n)
    right = [head]
    return recursion(head, right)

def recursion(head: ListNode, right: List[ListNode]) -> bool:
    if head.next is None:
        return
    head = head.next
    result = recursion(head, right)
    if result is False:
        return False
    result = right[0].val == head.val
    right[0] = right[0].next
    return result

# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
node4 = ListNode(1)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
result = isPalindrome(node1)
print("test1: ")
print(result)

node2 = ListNode(2)
node1 = ListNode(1, node2)
result = isPalindrome(node1)
print("test2: ")
print(result)

