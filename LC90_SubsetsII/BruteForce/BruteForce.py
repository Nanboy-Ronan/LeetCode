# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Input: nums = [0]
# Output: [[],[0]]

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Brute Force
        # Time Complexity: O(n*2^n)
        # Space Complexity: O(1)
        result = [[]]
        nums.sort()
        for num in nums:
            for ele in result:
                temp = ele + [num]
                if temp not in result:
                    result = result + [temp]
        return result
                