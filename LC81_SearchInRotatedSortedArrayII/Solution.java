/*
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.
*/

// 3 4 5 6 7     1 2
class Solution {
    // Binary Search
    // Time Complexity: O(logn)
    // Space Complexity: O(1)
    public boolean search(int[] nums, int target) {
        if(nums == null || nums.length == 0) return false;
        int left = 0, right = nums.length - 1;
        while(left <= right){
            int mid = right - (right - left) / 2;
            if(nums[mid] == target) return true;
            if(nums[left] == nums[right]){ // not sure which part is in order
                left++;
                continue;
            }
            if(nums[left] <= nums[mid]){ // left in order
                if(target >= nums[left] && target < nums[mid]){
                    right = mid - 1;
                }else{
                    left = mid + 1;
                }
            }else{ // right in order
                if(target > nums[mid] && target <= nums[right]){
                    left = mid + 1;
                }else{
                    right = mid - 1;
                }
            }
        }
        return false;
    }
}