from operator import truediv
from typing import List


class Solution:
    # DFS (backtrack)
    # Time Complexity: (2^n)
    # Space Complexity: (2^n)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return None
        self.track = []
        self.result = []
        self.target = target
        self.trackSum = 0

        self.backtrack(candidates, 0)
        return result

    def backtrack(self, candidates, start):
        if self.trackSum == self.target:
            self.result.append(self.track.copy())
            return
        if self.trackSum > self.target:
            return
        

        for i in range(start, len(candidates)):
            # print(self.result)
            self.track.append(candidates[i])
            self.trackSum += candidates[i]
            # print(self.track)
            # print(self.trackSum)
            self.backtrack(candidates, i)
            self.track.pop()
            self.trackSum -= candidates[i]

############################# Test ##########################
soln = Solution()
result = soln.combinationSum([2,3,6,7], 7)

        