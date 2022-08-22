from typing import Counter


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        substrings = []
        for x in range(len(s)):
            # x+1 is the length of the substring
            for i in range(len(s)-x):
                # i is the index 
                substrings.append(s[i:i+x+1])
        result = 0
        for substring in substrings:
            count = Counter(list(substring))
            if count['0'] == count['1']:
                count2 = Counter(list(substring[:len(substring)//2]))
                if count2['0'] == 0 or count2['1'] == 0:
                    result += 1
        return result