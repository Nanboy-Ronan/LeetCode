# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
# Input: root = [1]
# Output: [[1]]
# Input: root = []
# Output: []

from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root: TreeNode) -> List[List[int]]:
    # BFS
    # Time Complexity: O(n)
    # Space COmplexity: O(n)
    result = []
    if root is None:
        return result
    queue = deque([])
    temp = deque([])
    queue.append(root)
    while len(queue) != 0:
        size = len(queue)
        ls = []
        while size != 0:
            curr = queue.popleft()
            ls.append(curr.val)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
            size -= 1
        temp.appendleft(ls)
    result = list(temp)
    return result

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(levelOrderBottom(root1))

root2 = TreeNode(1)
print(levelOrderBottom(root2))

root3 = None
print(levelOrderBottom(root3))
    
