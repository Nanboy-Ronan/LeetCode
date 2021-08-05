# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Sort
        # Time Complexity: O(nlogn)
        # Space Complexity: O(1)
        nums.sort()
        return nums[len(nums)-k]