class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        // Two Pointers (slide window)
        // Time Complexity: O(n)
        // Space Complexity: O(1)
        int i = 0;
        int j = 0;
        int sum = 0;
        int result = nums.length + 1;
        while(j < nums.length){
            sum += nums[j];
            while(sum >= target){
                sum -= nums[i];
                result = Math.min(result, j - i + 1);
                i++;
            }
            j++;
        }
        return result == nums.length + 1? 0 : result;
    }
}