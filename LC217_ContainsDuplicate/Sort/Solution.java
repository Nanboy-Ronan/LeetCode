import java.util.Arrays;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Sort
        // Time Complexity: O(nlogn)
        // Space Complexity: O(1)
        if(nums.length == 0 || nums.length == 1){
            return false;
        }
        Arrays.sort(nums);

        int prev = 0;
        int curr = 1;

        while(curr < nums.length){
            if(nums[prev] == nums[curr]){
                return true;
            }
            prev++;
            curr++;
        }
        
        return false;
    }
}