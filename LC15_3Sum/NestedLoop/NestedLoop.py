# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    # Nested Loop with two Sum
    # Time Complexity: O(n^2)
    # Space Complexity: O(n) 
    def twoSum(nums: List[int], target: int) -> List[List[int]]:
        result = set() # must use set to prevent duplicate
        hashSet = set()
        for num in nums:
            temp = target - num
            if temp in hashSet:
                result.add((num, temp))
            hashSet.add(num) # must add after check to prevent use num itself twice
        return result

    if len(nums) < 3:
        return []

    nums.sort()
    result = set()
    # traverse every number and find pair that satisfy the sum
    for i in range(len(nums)):
        a = nums[i]
        target_pair_sum = 0 - a
        nums_remain = nums[i+1:]
        for b, c in twoSum(nums_remain, target_pair_sum):
            result.add((a,b,c))
    return result  

############################# Test #########################################
print(threeSum([-1,0,1,2,-1,-4]))