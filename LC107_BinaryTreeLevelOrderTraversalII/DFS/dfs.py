# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
# Input: root = [1]
# Output: [[1]]
# Input: root = []
# Output: []

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
    dfs(root, result, 0)
    result.reverse()
    return result

def dfs(node: TreeNode, result: List[List[int]], level: int):
    if node is None:
        return
    
    if level > len(result) - 1:
        result.append([])

    result[level].append(node.val)

    dfs(node.left, result, level+1)
    dfs(node.right, result, level+1)

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