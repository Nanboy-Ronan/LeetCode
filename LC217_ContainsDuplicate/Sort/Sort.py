# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Sort
        # Time Complexity: O(nlogn)
        # Space Complexity: O(1)
        if len(nums) == 0 or len(nums) == 1:
            return False
        
        nums.sort()

        prev = 0
        curr = 1

        while curr < len(nums):
            if nums[prev] == nums[curr]:
                return True
            else:
                prev += 1
                curr += 1
        
        return False
        