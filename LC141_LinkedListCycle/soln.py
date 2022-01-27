'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
'''

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Fast Slow Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return None
        fast, slow = head, head
        while fast.next is not None and fast.next.next is not None:
            fast, slow = fast.next.next, slow.next
            if fast == slow: # they will ultimately meed if there is a cycle
                return True
        return False
            




