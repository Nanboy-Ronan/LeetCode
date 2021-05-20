 # LeetCode 78 Subsets Given an integer array nums of unique elements, return
 # all possible subsets (the power set). The solution set must not contain
 # duplicate subsets. Return the solution in any order. Input: nums = [1,2,3]
 # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List


class subsets:
    # backtracing
    # Time Complexity: O(n#2^n)
    # Space Complexity: O(n#2^n)
    def __init__(self, set: List) -> None:
        self.set = set

    def main(self) -> None:
        result = self.subset(self.set)
        print(result)
        
    def subset(self, set: List[int]) -> List[List[int]]:
        result = [[]] # we start with an empty set (empty set is a subset of any set)
        for i in range(1, len(set)+1):
            self.backtracking(set, result, i, 0, [])
        return result
    
    def backtracking(self, nums, result, length, index, subset):
        # base case: stop when reaching the last element
        if len(subset) == length:
            result.append(subset[:])
            return
        
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.backtracking(nums, result, length, i+1, subset)
            subset.pop()
subset = subsets([1,2,3])
subset.main()