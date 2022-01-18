from typing import List


class Solution:
    # Two Pointers (backward)
    # Time Complexity: O(m+n)
    # Space Complexity: O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        curr = len(nums1) - 1
        nums1_index = m-1
        nums2_index = n-1
        while curr >= 0:
            if nums1_index < 0: # nums1 finished, all remain nums2
                nums1[curr] = nums2[nums2_index]
                nums2_index -= 1
                curr -= 1
            elif nums2_index < 0: # nums2 finished, all remain nums1
                nums1[curr] = nums1[nums1_index]
                nums1_index -= 1
                curr -= 1
            elif nums2[nums2_index] >= nums1[nums1_index]: # the end of num2 is largest
                nums1[curr] = nums2[nums2_index]
                nums2_index -= 1
                curr -= 1
            else:
                nums1[curr] = nums1[nums1_index]
                nums1_index -= 1
                curr -= 1