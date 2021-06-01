# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Input: head = [1,2]
# Output: [2,1]
# Input: head = []
# Output: []

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    # Iteration
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    if head is None:
        return None
    temp1 = head
    temp2 = head.next
    newHead = head

    while temp2 is not None:
        temp1.next = temp2.next
        temp2.next = newHead
        newHead = temp2
        temp2 = temp1.next

    return newHead

# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
node5 = ListNode(5)
node4 = ListNode(4,node5)
node3 = ListNode(3,node4)
node2 = ListNode(2,node3)
node1 = ListNode(1,node2)
result = reverseList(node1)
print("test1: ")
while(result != None):
            print(result.val)
            result = result.next

node2 = ListNode(2)
node1 = ListNode(1,node2)
result = reverseList(node1)
print("test2: ")
while(result != None):
            print(result.val)
            result = result.next

node = None
result = reverseList(node)
print("test3: ")
while(result != None):
            print(result.val)
            result = result.next
