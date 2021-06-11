# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs

from typing import List
from TreeNode import TreeNode


def sortedArrayToBST(nums: List[int]) -> TreeNode:
    if len(nums) == 0:
        return None
    
    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

    return root

# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
result = sortedArrayToBST([-10,-3,0,5,9])
print("test 1: ")
result.display()

result = sortedArrayToBST([1,3])
print("test 2: ")
result.display()