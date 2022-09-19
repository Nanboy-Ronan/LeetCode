from typing import List


class Solution:
    # Dynamic Programming
    # Time Comlplexity: O(n^2)
    # Space Complexity: O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(len(s)):
            if dp[i] is True:
                # match the next substring
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        dp[i+len(word)] = True
        
        return dp[-1]

########################### Test #########################
soln = Solution()
print(soln.wordBreak("leetcode", ["leet", "code"]))