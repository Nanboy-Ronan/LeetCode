# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Input: n = 1
# Output: ["()"]

from typing import List


def generateParenthesis(n: int) -> List[str]:
    result = []
    backTrack(n,result,0,0,"")
    return result

def backTrack(n: int, result: List[str], left: int, right: int, subset: str) -> None:
    # BackTracking
    # Time Complexity: O(combine(n))
    # Space Complxity: O(combine(n))
    if left < right or left > n or right > n:
        return

    if right == n and left == n and right == left:
        result.append(subset)
        return

    components = ["(",")"]

    for component in components:
        subset += component
        if component == "(":
            backTrack(n,result,left+1,right,subset)
        elif component == ")":
            backTrack(n,result,left,right+1,subset)
        subset = subset[:-1]

# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print("test 1: ")
print(generateParenthesis(3))

print("test 2: ")
print(generateParenthesis(1))
    
    