# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
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

def levelOrder(root: TreeNode) -> List[List[int]]:
    # BFS
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    result = []
    if root is None:
        return result
    
    ## BFS
    queue = deque([])
    queue.append(root)
    while len(queue) > 0: # a new level
        size = len(queue)
        list = []
        while size > 0:
            curr = queue.popleft()
            list.append(curr.val)
            ## add all its children
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
            size -= 1
        result.append(list)
    return result

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(levelOrder(root1))

root2 = TreeNode(1)
print(levelOrder(root2))

root3 = None
print(levelOrder(root3))