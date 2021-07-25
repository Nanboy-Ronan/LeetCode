# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Input: nums = [0]
# Output: [[],[0]]

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # DFS
        # Time Complexity: O(n*2^n)
        # Space Complexity: O(n*2^n)
        result = []
        nums.sort()
        self.dfs(nums,[],result)
        return result

    def dfs(self, nums: List[int], curr: List[List[int]], result: List[List[int]]):
        result.append(curr)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:],curr+[nums[i]],result)