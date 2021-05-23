# LeetCode 78 Subsets Given an integer array nums of unique elements, return
# all possible subsets (the power set). The solution set must not contain
# duplicate subsets. Return the solution in any order. Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List

# dfs
# Time Complexity: O(n#2^n)
# Space Complexity: O(n#2^n)
def subsets(set: List[int]) -> List[List[int]]:
    result = []
    dfs(set, result, 0, [])
    return result

def dfs(set: List[int], result: List[List[int]], index: int, subset: List[int]) -> None:
    result.append(subset[:])
    if index == len(set):
        return
    for i in range(index, len(set)):
        subset.append(set[i])
        dfs(set, result, i+1, subset)
        subset.pop()


# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print(subsets([1,2,3]))