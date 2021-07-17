class Solution {
    // Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    // Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    // Output: 6
    // Explanation: [4,-1,2,1] has the largest sum = 6.
    // Input: nums = [1]
    // Output: 1
    // Input: nums = [5,4,-1,7,8]
    // Output: 23
    public int maxSubArray(int[] nums) {
        // Dynamic Programming
        // Time Complexity: O(n)
        // Space COmplexity: O(n)
        int result = nums[0];
        int temp = nums[0];
        for(int i = 1; i < nums.length; i++){
            temp = Math.max(temp+nums[i], nums[i]); // ensure get max in a continuous array
            result = Math.max(result, temp);  // ensure get max from all continuous subarrays
        }
        return result;
        
    }
}