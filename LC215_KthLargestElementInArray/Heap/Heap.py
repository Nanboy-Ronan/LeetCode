# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Heap
        # Time Complexity: O(nlog(k)) kth largest element in an array
        # Space Complexity: O(1)
        min_heap = []
        heapq.heapify(min_heap)

        for num in nums:
            heapq.heappush(min_heap,num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]