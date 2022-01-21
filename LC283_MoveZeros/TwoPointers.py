from typing import List


class Solution:
    # Two pointers
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # idea: traverse tje array and put all non zeros in front together, put zeros to the rest
        i = 0
        j = 0 # j is the number of non-zeros
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        nums[j:] = [0]*(len(nums)-j)