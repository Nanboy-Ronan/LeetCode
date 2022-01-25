import java.util.ArrayList;
import java.util.List;

class Solution {
    // Traverse and math
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n = nums.length;
        for(int num : nums){
            int true_value = (num-1) % n;
            if(nums[true_value] <= n){
                nums[true_value] += n;
            }
        }

        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < n; i++){
            if(nums[i] <= n){
                result.add(i+1);
            }
        }
        return result;
    }
}