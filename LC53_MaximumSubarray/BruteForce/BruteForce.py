# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Input: nums = [1]
# Output: 1
# Input: nums = [5,4,-1,7,8]
# Output: 23

from typing import List


def maxSubArray(self, nums: List[int]) -> int:
    # Brute Force
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    # This will exceed the time limit
    result = float('-inf')
    for i in range(len(nums)):
        temp = 0
        for j in range(i,len(nums)):
            temp += nums[j]
            result = max(temp,result)
    return result