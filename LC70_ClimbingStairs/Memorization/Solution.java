import java.util.HashMap;

class Solution {
    // Recursion and Memorization
    // Time Complxity: O(n)
    // Space Complexity: O(m)
    HashMap<Integer, Integer> mapping = new HashMap<>();
    public int climbStairs(int n) {
        if(n == 1) return 1;
        if(n == 2) return 2;
        if(mapping.get(n) == null){
            int result = climbStairs(n-1) + climbStairs(n-2);
            mapping.put(n, result);
            return result;
        }
        return mapping.get(n);
    }
}