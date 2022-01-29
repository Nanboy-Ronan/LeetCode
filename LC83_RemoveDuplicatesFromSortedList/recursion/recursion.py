# Definition for singly-linked list.
from typing import Optional

from numpy import delete


class ListNode:
    # recursion
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head
