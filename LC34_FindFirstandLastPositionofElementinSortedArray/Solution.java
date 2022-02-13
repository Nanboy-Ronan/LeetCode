class Solution {
    // Binary Search
    // Time Complexity: O(logn)
    // Space Complexity: O(1)
    public int[] searchRange(int[] nums, int target) {
        int[] result = new int[] {-1,-1};
        if(nums.length == 0){
            return result;
        }
        // find the first occurence
        int left = 0, right = nums.length - 1;
        while(left < right){
            int mid = (left+right)/2;
            if(nums[mid] >= target){
                right = mid;
            }else{
                left = mid + 1;
            }
        }

        // If no such target exists
        if(nums[left] != target){
            return result;
        }

        // add first occurence to result
        result[0] = left;

        // Find last occurence
        left = 0; right = nums.length - 1;
        while(left < right){
            int mid = right - (right - left)/2;
            if(nums[mid] <= target){
                left = mid;
            }else{
                right = mid - 1;
            }
        }
        result[1] = left;

        return result;
    }
}