# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Input: head = []
# Output: []
# Input: head = [1]
# Output: [1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    # recursion
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    if head is None or head.next is None:
        return head
    
    next = head.next
    head.next = swapPairs(next.next)
    next.next = head
    return next

# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
t1node4 = ListNode(4)
t1node3 = ListNode(3, t1node4)
t1node2 = ListNode(2, t1node3)
t1node1 = ListNode(1, t1node2)

result = swapPairs(t1node1)
print("test1: ")
while(result != None):
    print(result.val)
    result = result.next


t2node5 = ListNode(5)
t2node4 = ListNode(4, t2node5)
t2node3 = ListNode(3, t2node4)
t2node2 = ListNode(2, t2node3)
t2node1 = ListNode(1, t2node2)

result = swapPairs(t2node1)
print("test2: ")
while(result != None):
            print(result.val)
            result = result.next


result = swapPairs(None)
print("test3: ")
while(result != None):
            print(result.val)
            result = result.next


t4node1 = ListNode(1)
result = swapPairs(t4node1)
print("test4: ")
while(result != None):
            print(result.val)
            result = result.next