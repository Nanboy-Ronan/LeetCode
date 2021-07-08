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
    # Hash
    # Time Complexity: O(nk)
    # Space Complexity: O(nk)
    if len(strs) <= 1:
        return [strs]
    
    result = {}

    # count the number of each letter in the word
    for str in strs:
        count_table = [0]*26 # [0,0,0...,0]
        for char in str:
            # ord('a'): 97
            # ord('b'): 98
            # ord('c'): 99
            count_table[ord(char)-ord('a')] += 1 # add one in each index correspond to the letter
        # if count_table is the same, then same word but different sequence of letter
        key = tuple(count_table) # tuple is hashable while list is not
        result[key] = result.get(key,[]) + [str]
    return result.values()

# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
print("test 1: ")
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

print("test 2: ")
print(groupAnagrams([""]))

print("test 3: ")
print(groupAnagrams(["a"]))