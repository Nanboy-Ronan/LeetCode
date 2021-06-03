# Given the head of a singly linked list, return true if it is a palindrome.
# Input: head = [1,2,2,1]
# Output: true
# Input: head = [1,2]
# Output: false


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    # recursion
    # Time Complexity: O(n)
    # Space COmplexity： O(1)
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    if fast is not None:
        slow = slow.next
    
    laterHalf = reverseLinkedList(slow)

    while laterHalf is not None:
        if head.val != laterHalf.val:
            return False
        head = head.next
        laterHalf = laterHalf.next
    return True

def reverseLinkedList(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
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
t1node4 = ListNode(1)
t1node3 = ListNode(2, t1node4)
t1node2 = ListNode(2, t1node3)
t1node1 = ListNode(1, t1node2)
result = isPalindrome(t1node1)
print("test1: ")
print(result)

t2node5 = ListNode(1)
t2node4 = ListNode(2, t2node5)
t2node3 = ListNode(3, t2node4)
t2node2 = ListNode(2, t2node3)
t2node1 = ListNode(1, t2node2)
result = isPalindrome(t2node1)
print("test2: ")
print(result)

t3node2 = ListNode(2)
t3node1 = ListNode(1, t3node2)
result = isPalindrome(t3node1)
print("test3: ")
print(result)