'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
'''

from typing import List


class Solution:
    # Pointers
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return None
        nums.sort()
        result = float('inf')
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    return sum
                elif sum < target:
                    l += 1
                else:
                    r -= 1
                if abs(target - sum) < abs(result - target):
                    result = sum
        return result

############################## Test #################################
test = Solution()
result = test.threeSumClosest([-1,2,1,-4], 1)
print(result)

result = test.threeSumClosest([1,1,1,0],-100)
print(result)
        