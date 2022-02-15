'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
'''

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 0:
            return [-1,-1]
        l, r = 0, len(nums)-1
        # find the first element
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        # case that no such target exist
        if nums[l] != target:
            return [-1,-1]
        result = []
        result.append(l)
        # find the second argument
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else: 
                r = mid - 1
        result.append(l)
        return result

################################# Test ##################################
nums = [5,7,7,8,8,10]
target = 8

test = Solution()
result = test.searchRange(nums,target)
print(result)
        