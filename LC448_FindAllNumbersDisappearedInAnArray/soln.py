'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
'''


from typing import List


class Solution:
    # Traverse
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # idea: traverse the array, return the index where holds number still in n
        n = len(nums)
        result = []
        for num in nums:
            temp = (num-1)%n # necessay, because it change the element that has not been traversed
            if temp <= n-1:
                nums[temp] += n # within the range, eliminate it
        for i in range(len(nums)):
            if nums[i] <= n: # not being eliminated
                result.append(i+1)
        return result

######################## Test ###########################
test = Solution()
print(test.findDisappearedNumbers([4,3,2,7,8,2,3,1]))