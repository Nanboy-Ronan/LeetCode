# Definition for a binary tree node.
from collections import deque
from operator import le
from tabnanny import check


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # BFS
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def check(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val == node2.val:
            return True
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        queue1 = deque()
        queue2 = deque()
        queue1.append(p)
        queue2.append(q)

        while(len(queue1) > 0):
            if len(queue1) != len(queue2):
                return False
            length = len(queue1)
            for _ in range(length):
                pNode = queue1.popleft()
                qNode = queue2.popleft()
                if not self.check(pNode, qNode):
                    return False
                if pNode is not None:
                    queue1.append(pNode.left)
                    queue1.append(pNode.right)
                if qNode is not None:
                    queue2.append(qNode.left)
                    queue2.append(qNode.right)
        if len(queue2) != 0:
            return False
        return True
 