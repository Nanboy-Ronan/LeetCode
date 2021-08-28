# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Bit Manipulation
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        if n < 1:
            return False
        
        return (n & (n-1)) == 0