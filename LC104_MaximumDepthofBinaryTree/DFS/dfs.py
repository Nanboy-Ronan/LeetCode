# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS
    # Time Complexty: O(n)
    # Space Complexity: O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.dfs(root)
    
    def dfs(self, node):
        lLeft = 0
        lRight = 0
        if node.left is not None:
            self.dfs(node.left)
        if node.right is not None:
            self.dfs(node.right)
        return max(lLeft, lRight) + 1