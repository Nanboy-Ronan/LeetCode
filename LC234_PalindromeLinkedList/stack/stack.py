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
    # stack
    # Time Complexity: O(n)
    # Space COmplexity： O(n)
    stack = []
    curr = head
    while curr is not None:
        stack.append(curr.val)
        curr = curr.next

    while head is not None:
        if head.val != stack.pop():
            return False
        head = head.next
    return True


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