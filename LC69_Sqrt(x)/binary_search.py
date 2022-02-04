'''
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
'''


class Solution:
    # Binary Search
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 1, x//2
        while l <= r:
            mid = l + (r - l) // 2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                r = mid - 1
            else:
                l = mid + 1
        
        return r
