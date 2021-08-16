# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Hash Map
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        if len(nums) == 0:
            return False

        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 0
            mapping[num] += 1
        
        for value in mapping.values():
            if value > 1:
                return True
        return False