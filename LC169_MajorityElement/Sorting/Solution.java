import java.util.Arrays;

class Solution {
    public int majorityElement(int[] nums) {
        // Sort
        // Time Complexity: O(n*logn)
        // Space Complexity: O(1)
        Arrays.sort(nums);
        return nums[nums.length/2];
    }
}