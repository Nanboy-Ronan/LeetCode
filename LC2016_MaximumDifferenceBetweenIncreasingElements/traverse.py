# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # Traverse
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        minimum = float('inf')
        result = 0
        for num in nums:
            minimum = min(minimum, num)
            result = max(result, nums - minimum)
        return result if result > 0 else -1