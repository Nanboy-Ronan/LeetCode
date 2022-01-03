'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
'''

from typing import List


class Solution:
    # Pointers
    # Time Complexity: O(n^3)
    # Space Complexity: O(1)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        result = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l, h = j+1, len(nums) - 1
                while l < h:
                    sum = nums[i] + nums[j] + nums[l] + nums[h]
                    if sum == target:
                        result.append([nums[i], nums[j], nums[l], nums[h]])
                        while l < h and nums[l] == nums[l+1]: # necessay to check l < h because index may run over the array
                            l += 1
                        # while nums[h] == nums[h-1]:
                        #     h -= 1
                        l += 1
                        # h -= 1
                    elif sum < target:
                        l += 1
                    else:
                        h -= 1
        return result

################################### Test #########################################
test = Solution()
result = test.fourSum([1,0,-1,0,-2,2], 0)
print(result)