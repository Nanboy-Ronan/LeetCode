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
    # iteration
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    if head is None or head.next is None:
        return head
        
    temp1 = head
    temp2 = head.next
    prev = ListNode
    
    head = head.next

    while temp2 is not None and temp2.next is not None:
        temp3 = temp2.next
        temp2.next = temp1
        temp1.next = temp3
        prev.next = temp2
        prev = temp1

        temp2 = temp3.next
        temp1 = temp3
    
    if temp2 is None:
        return head
    elif temp2.next is None:
        temp3 = temp2.next
        temp2.next = temp1
        temp1.next = temp3
        prev.next = temp2
        return head

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