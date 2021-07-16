# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Input: nums = [1]
# Output: 1
# Input: nums = [5,4,-1,7,8]
# Output: 23

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Dynamic Programming
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            result = max(dp[i],result)
        return result
        