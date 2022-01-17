'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

from typing import List


class Solution:
    # Traverse
    # Time Complexity: O(nm) n is the length of str and m is the length of the prefix
    # Space Complexity: O(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            # traverse the rest of strings
            for str in strs:
                # return only if one prefix does not match
                if len(str) - 1 < i:
                    return str
                elif str[i] != strs[0][i]:
                    return strs[0][0:i]
                else: # prefix are all matching
                    pass
        return strs[0] # only first string

################################ Solution #####################################
test = Solution()
result = test.longestCommonPrefix(["flower","flow","flight"])
print(result)