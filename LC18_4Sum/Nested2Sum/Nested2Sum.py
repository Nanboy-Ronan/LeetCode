'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
'''

from typing import List


class Solution:
    # Nested two and three sum
    # Time Complexity: O(n^3)
    # Space Complexity: O(n^2)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            if len(nums) < 2:
                return []
            hash_set = set()
            result = set()
            for i in range(len(nums)):
                temp = target - nums[i]
                if temp in hash_set:
                    result.add((nums[i], temp))
                hash_set.add(nums[i])
            return result

        def threeSum(nums: List[int], target: int) -> List[List[int]]:
            if len(nums) < 3:
                return []
            result = set()
            for i in range(len(nums) - 2):
                temp = target - nums[i]
                for b, c in twoSum(nums[i+1:], temp):
                    result.add((nums[i], b, c))
            return result
            

        if len(nums) < 4:
            return []
        nums.sort()
        result = set()
        for i in range(len(nums) - 3):
            temp = target - nums[i]
            for b, c, d in threeSum(nums[i+1:], temp):
                result.add((nums[i], b, c, d))
        return result

################################## Test ##########################################
test = Solution()
result = test.fourSum([1,0,-1,0,-2,2], 0)
print(result)

