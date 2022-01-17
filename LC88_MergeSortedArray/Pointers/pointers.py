from typing import List


class Solution:
    # Two Pointers
    # Time Complexity: O(m+n)
    # Space Complexity: O(m+n)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index = 0
        nums2_index = 0
        temp = []
        for i in range(m):
            # if one index is ready reaches the end, necessary to avoid index out of the length of the array
            if nums1_index >= m:
                temp += nums2[nums2_index:]
                break
            elif nums2_index >= n:
                temp += nums1[nums1_index:m]
                break
            elif nums1[nums1_index] <= nums2[nums2_index]:
                temp.append(nums1[nums1_index])
                nums1_index += 1
            else:
                temp.append(nums2[nums2_index])
                nums2_index += 1
        for i in range(len(nums1)):
            nums1[i] = temp[i]