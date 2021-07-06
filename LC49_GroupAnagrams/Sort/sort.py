# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Input: strs = [""]
# Output: [[""]]
# Input: strs = ["a"]
# Output: [["a"]]

from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # Sort
    # Time Complexity: O(nklog(k))
    # Space Complexity: O(nk)
    if len(strs) <= 1:
        return [strs]
    
    # sorted("cba") -> ['c','b','a']
    # ''.join(sorted("cba")) -> 'abc'

    # dict[key] -> value
    # dict.values() -> list of values
    # dict.get(x,y), x is the key, y is the default value (return when not found)
    result = {}

    for str in strs:
        sort = ''.join(sorted(str))
        result[sort] = result.get(sort,[]) + [str]
    
    return result.values()

# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
print("test 1: ")
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

print("test 2: ")
print(groupAnagrams([""]))

print("test 3: ")
print(groupAnagrams(["a"]))