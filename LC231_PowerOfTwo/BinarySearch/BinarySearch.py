# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Binary Search
        # Time Complexity: O(logn)
        # Space Complexity: O(1)
        # Time limit exceeded
        if n < 1:
            return False
        
        start = 0
        end = n

        while start <= end:
            mid = start + (end - start) // 2
            result = pow(2,mid)
            if result == n:
                return True
            elif result < n:
                start = mid + 1
            else:
                end = mid - 1
        
        return False