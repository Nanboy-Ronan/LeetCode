from typing import List


class Solution:
    # Hash Set
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        hashSet = set(nums)
        bestSoFar = 1

        for num in nums:
            if num-1 not in hashSet:
                temp = num + 1
                count = 1
                while temp in hashSet:
                    count += 1
                    temp += 1
                bestSoFar = max(bestSoFar, count)
        return bestSoFar