 # LeetCode 78 Subsets Given an integer array nums of unique elements, return
 # all possible subsets (the power set). The solution set must not contain
 # duplicate subsets. Return the solution in any order. Input: nums = [1,2,3]
 # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List


class subsets:
    # brute force
    # Time Complexity: O(n#2^n)
    # Space Complexity: O(n#2^n)
    def __init__(self, set: List) -> None:
        self.set = set
    
    def main(self) -> None:
        result = self.subset(self.set)
        print(result)
    
    def subset(self, set: List) -> List[List[int]]:
        result = [[]] # we start with an empty set (empty set is a subset of any set)

        for num in set:
            temp = [] # temp hold all the subsets after adding the next number
            for subset in result:
                temp.append(subset+[num])
            
            result = result + temp # append temp to result
        return result
test = subsets([1,2,3])
test.main()