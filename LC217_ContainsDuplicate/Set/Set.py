# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Set
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        if len(nums) == 0:
            return False
        
        hashSet = set(nums)
        return False if len(nums) == len(hashSet) else True