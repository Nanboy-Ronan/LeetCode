# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Input: nums = [3,3], target = 6
# Output: [0,1]

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # Hash Table
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    result = []
    hashTable = {}
    for i in range(0, len(nums)):
        hashTable[nums[i]] = i
    for i in range(0, len(nums)):
        diff = target - nums[i]
        if(diff in hashTable and hashTable[diff] != i):
            result.append(i)
            result.append(hashTable[diff])
            return result

# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))