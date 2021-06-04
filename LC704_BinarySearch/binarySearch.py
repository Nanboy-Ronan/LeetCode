# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

from typing import List


def search(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)-1

    while left <= right:
        mid = right - (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1

# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print("test1: ")
print(search([-1,0,3,5,9,12], 9)) # 4

print("test2: ")
print(search([-1,0,3,5,9,12,13], 13)) # 6

print("test3: ")
print(search([-1,0,3,5,9,12], 2)) # -1