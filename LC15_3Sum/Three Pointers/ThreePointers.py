'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
'''

from typing import List


class Solution:
    # Three Pointers
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue # prevent [-4, -1, -1, -1, -1, 1, 3]
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l< r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return result

########################### Test ###################################
test = Solution()
result = test.threeSum([-1,0,1,2,-1,-4])
print(result)

result = test.threeSum([0,0,0])
print(result)