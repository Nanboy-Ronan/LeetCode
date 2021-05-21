 # LeetCode 78 Subsets Given an integer array nums of unique elements, return
 # all possible subsets (the power set). The solution set must not contain
 # duplicate subsets. Return the solution in any order. Input: nums = [1,2,3]
 # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List
# the track the length of the set from 0, 1, 2 ...
# every time increment the target length by 1

class subsets:
    # backtracking
    # Time Complexity: O(n#2^n)
    # Space Complexity: O(n#2^n)
    def __init__(self, set: List[int]) -> None:
        self.set = set

    def main(self) -> None:
        result = self.subset(self.set)
        print(result)
        
    def subset(self, set: List[int]) -> List[List[int]]:
        result = [[]] # we start with an empty set (empty set is a subset of any set)
        for i in range(1, len(set)+1): # this is the length of subset starting from 1 (length 0 has been added in the previous line)
            self.backtracking(set, result, i, 0, [])
        return result
    
    # MODIFY: result
    # set is the given set
    # result is the output
    # length is the length of the subset for this backtrack
    # index indicate the next element starting backtrack (we dismiss the current element in this question to avoid repetition)
    def backtracking(self, set: List[int], result: List[List[int]], length, index, subset) -> None:
        # base case: stop when reaching the last element
        if len(subset) == length:
            result.append(subset[:])
            return
        
        for i in range(index, len(set)):
            subset.append(set[i])
            self.backtracking(set, result, length, i+1, subset)
            # delete the currenlt element so backtrack works
            subset.pop()

subset = subsets([1,2,3])
subset.main()