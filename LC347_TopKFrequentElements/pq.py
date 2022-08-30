from heapq import heappop, heappush, heapreplace
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return None
        # Count the number of elements
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Create priority queue for k largest elements
        pq = [] # min heap
        for ele, freq in count.items():
            if len(pq) < k:
                heappush(pq, (freq, ele))
            elif freq > pq[0][0]:
                heapreplace(pq, (freq, ele))
        
        # Get the result
        result = []
        for _ in range(len(pq)):
            result.append(heappop(pq))
        return result
