import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums){
        // Backtrack
        // Time Complexity: O(n*2^n)
        // Space Complexity: O(n*2^n)
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();

        Arrays.sort(nums);
        for(int i = 0; i <= nums.length; i++){
            backTrack(nums, i, 0, subset, result);
        }
        return result;
    }

    private void backTrack(int[] nums, int length, int index, List<Integer> subset, List<List<Integer>> result){
        if(subset.size() == length){
            result.add(new ArrayList<>(subset));
            return;
        }

        for(int i = index; i < nums.length; i++){
            if(i > index && nums[i] == nums[i-1]){
                continue;
            }
            subset.add(nums[i]);
            backTrack(nums, length, i+1, subset, result);
            subset.remove(subset.size()-1);
        }
    }
}
