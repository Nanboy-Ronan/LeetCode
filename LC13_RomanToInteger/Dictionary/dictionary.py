class Solution:
    # Traverse
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def romanToInt(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = mapping[s[0]]
        for i in range(1,len(s)):
            if mapping[s[i]] > mapping[s[i-1]]:
                result += mapping[s[i]] - 2*mapping[s[i-1]]
            else:
                result += mapping[s[i]]
        return result