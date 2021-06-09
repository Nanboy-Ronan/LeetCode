# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Input: l1 = [], l2 = []
# Output: []
# Input: l1 = [], l2 = [0]
# Output: [0]

from typing import List


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # recursion
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    if l1 is None or l2 is None:
        return l1 or l2
    if l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
## test 1
t1node3 = ListNode(4)
t1node2 = ListNode(2, t1node3)
t1node1 = ListNode(1, t1node2)

t1node6 = ListNode(4)
t1node5 = ListNode(3, t1node6)
t1node4 = ListNode(1, t1node5)

result = mergeTwoLists(t1node1, t1node4)
print("test1: ")
while(result != None):
    print(result.val)
    result = result.next

## test 2
result = mergeTwoLists(None, None)
print("test2: ")
while(result != None):
    print(result.val)
    result = result.next

## test 3
t3node1 = None
t3node2 = ListNode(0)

result = mergeTwoLists(t3node1, t3node2)
print("test3: ")
while(result != None):
    print(result.val)
    result = result.next