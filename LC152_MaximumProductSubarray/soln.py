from math import prod
from typing import List


class Solution:
    # Traverse
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxProduct(self, nums: List[int]) -> int:
        maxA = [nums[0]]
        minA = [nums[0]]
        for i in range(1, len(nums)):
            maxA = max(maxA[i-1]*nums[i], nums[i], minA[i-1]*nums[i])
            minA = min(maxA[i-1]*nums[i], nums[i], minA[i-1]*nums[i])
        return max(maxA)