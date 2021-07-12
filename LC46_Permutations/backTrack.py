# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Input: nums = [1]
# Output: [[1]]


from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    if len(nums) == 0:
        return [[]]
    
    result = []
    visited = {}

    for num in nums:
        visited[num] = False
    
    backTrack(nums, [], visited, result)

    return result

def backTrack(nums: List[int], subset: List[int], visited: map,result: List[List[int]]) -> None:
    if len(subset) == len(nums):
        result.append(subset[:])
        return
    
    for num in nums:
        if not visited[num]:
            subset.append(num)
            visited[num] = True
            backTrack(nums, subset, visited, result)
            visited[subset[-1]] = False
            subset.pop()


# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
print("test 1: ")
print(permute([1,2,3]))

print("test 2: ")
print(permute([0,1]))

print("test 3: ")
print(permute([1]))