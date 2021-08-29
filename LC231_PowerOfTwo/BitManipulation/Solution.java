class Solution {
    public boolean isPowerOfTwo(int n) {
        // Bit Manipulation
        // Time Complexity: O(1)
        // Space Complexity: O(1)
        if(n < 1){
            return false;
        }

        return (n&(n-1)) == 0;
        
    }
}