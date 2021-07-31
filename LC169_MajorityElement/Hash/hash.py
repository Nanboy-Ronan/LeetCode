# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Hash
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 0
            mapping[num] = mapping[num] + 1
        half_length = len(nums) // 2
        for key in mapping:
            if mapping[key] > half_length:
                return key