/*
Reverse bits of a given 32 bits unsigned integer.
*/

public class Solution {
    // you need treat n as an unsigned value
    // Bit wise Operation
    // Time complexity: O(logn)
    // Space complexity: O(1)
    public int reverseBits(int n) {
        int result = 0;
        for(int i = 0; i < 32; i++){
            result <<= 1;
            result += n & 1;
            n >>= 1;
        }
        return result;
    }
}