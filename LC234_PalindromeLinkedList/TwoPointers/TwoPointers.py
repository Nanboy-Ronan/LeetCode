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
    # Two Pointers
    # Time Complexity: O(n)
    # Space COmplexity： O(n)
    if head is None or head.next is None:
        return True
    temp = []
    curr = head
    while curr is not None:
        temp.append(curr.val)
        curr = curr.next
    left = 0
    right = len(temp)-1
    while left < right:
        if temp[left] != temp[right]:
            return False
        left += 1
        right -= 1
    return True

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
