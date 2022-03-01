import java.util.ArrayList;
import java.util.List;

class Solution {
    // Quick Select
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int findKthLargest(int[] nums, int k) {
        int left = 0;
        int right = nums.length - 1;
        while(true){
            int pivot = partition(nums, left, right);
            if(pivot == k - 1) return nums[pivot];
            if(pivot > k - 1) right = pivot - 1;
            else left = pivot + 1;
            
        }
    }


    void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    int partition(int[] nums, int left, int right){
        int pivot = left;
        for(int i = left; i < right; i++){
            if(nums[i] > nums[right]){
                swap(nums, i, pivot);
                pivot++;
            }
        }
        swap(nums, pivot, right);
        return pivot;
    }

}