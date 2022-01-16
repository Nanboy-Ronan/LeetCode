class Solution {
    // Dynamic Programming
    public int climbStairs(int n) {
        if(n == 1) return 1;
        if(n == 2) return 2;
        // for n = 3
        int result = 0;
        int prePre = 1;
        int pre = 2;
        for(int i = 3; i <= n; i++){
            result = prePre + pre;
            prePre = pre;
            pre = result;
        }
        return result;
    }
}