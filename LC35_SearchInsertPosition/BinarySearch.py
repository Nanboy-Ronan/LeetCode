# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# Input: nums = [1,3,5,6], target = 0
# Output: 0
# Input: nums = [1], target = 0
# Output: 0

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    # Binary Search
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    if nums is None or len(nums) == 0:
        return 0
    
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = right - (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left+1 if nums[left] < target else left


# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print("test 1: ")
print(searchInsert([1,3,5,6],5))

print("test 2: ")
print(searchInsert([1,3,5,6],2))

print("test 3: ")
print(searchInsert([1,3,5,6],7))

print("test 4: ")
print(searchInsert([1,3,5,6],0))

print("test 5: ")
print(searchInsert([1],0))