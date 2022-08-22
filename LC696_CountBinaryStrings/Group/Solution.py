# Idea: Only need to count the number of either zero or one

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Groups
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1
        result = 0
        for i in range(1, len(groups)):
            result += min(groups[i-1], groups[i])
        return result