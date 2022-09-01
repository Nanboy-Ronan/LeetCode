class Solution:
    # Sliding Window
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        substring = {}
        left = 0
        right = 0
        result = 0
        while right < len(s):
            if s[right] not in substring:
                # Character hasn't been visited
                substring[s[right]] = right
            else:
                # Charater has been visited
                lastOcc = substring[s[right]]
                for i in range(left, substring[s[right]]+1):
                    substring.pop(s[i])
                left = lastOcc + 1
                substring[s[right]] = right

            result = max(result, right - left + 1)
            right += 1
        return result

########################### Test ######################
soln = Solution()
soln.lengthOfLongestSubstring("abcabcbb")