/*
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
*/

class Solution {
    // Binary Search
    // Time Complexity: O(logn)
    // Space Complexity: O(1)
    public int mySqrt(int x) {
        if(x < 2){
            return x;
        }
        int left = 1, right = x / 2;
        while(left <= right){
            long middle = left + (right - left) / 2;
            if(middle*middle == x){
                return (int)middle;
            }else if(middle*middle > x){
                right = (int)middle - 1;
            }else{
                left = (int)middle + 1;
            }
        }
        return right;
    }
}