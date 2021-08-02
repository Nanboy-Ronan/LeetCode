# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Brute Force
        # Time Limit Exceeded
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        for length in range(1,len(nums)+1):
            for i in range(len(nums)):
                if sum(nums[i:i+length]) >= target:
                    return length
        return 0 
