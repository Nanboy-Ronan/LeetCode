# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Two pointers (sliding windows)
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if nums is None or len(nums) == 0:
            return 0
        
        result = len(nums) + 1
        i,j = 0,0
        sum = 0
        while j < len(nums):
            sum += nums[j]
            while sum >= target and i < len(nums):
                result = min(result,j-i+1)
                sum -= nums[i]
                i += 1
            j += 1
        
        return 0 if result == len(nums)+1 else result