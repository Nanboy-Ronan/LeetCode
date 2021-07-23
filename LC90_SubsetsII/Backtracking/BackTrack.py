# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Input: nums = [0]
# Output: [[],[0]]

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Backtrack
        # Time Complexity: O(n*2^n)
        # Space Complexity: O(n*2^n)
        result = []

        nums.sort()
        for i in range(len(nums)+1):
            self.backTrack(nums,i,0,result,[])
        return result
        
    
    def backTrack(self, nums: List[int], length: int, index: int, result: List[List[int]], subset: List[int]) -> None:
        if len(subset) == length:
            result.append(subset[:])
            return
        
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.backTrack(nums,length,i+1,result,subset)
            subset.pop()