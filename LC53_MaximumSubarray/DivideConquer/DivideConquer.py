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
        # Divide and Conquer
        # Time Complexity: O(n)
        # Space Complexity: O(logn)
        return self.getMax(nums,0,len(nums)-1)
    
    def getMax(self, nums: List[int], lIndex: int, rIndex: int) -> int:
        if lIndex == rIndex:
            return nums[lIndex]
        midIndex = lIndex + (rIndex - lIndex) // 2
        leftSum = self.getMax(nums,lIndex,midIndex)
        rightSum = self.getMax(nums,midIndex+1,rIndex)
        crossSum = self.crossSum(nums,lIndex,rIndex)
        return max(leftSum,rightSum,crossSum)
    
    def crossSum(self, nums: List[int], lIndex: int, rIndex: int):
        midIndex = lIndex + (rIndex-lIndex) // 2

        leftSum = nums[midIndex]
        leftMax = leftSum
        for i in range(midIndex-1,lIndex-1,-1): # range(a,b) -> [a,b)
            leftSum += nums[i]
            leftMax = max(leftMax,leftSum)
        
        rightSum = nums[midIndex+1]
        rightMax = rightSum
        for i in range(midIndex+2,rIndex+1):
            rightSum += nums[i]
            rightMax = max(rightMax,rightSum)
        
        return leftMax + rightMax