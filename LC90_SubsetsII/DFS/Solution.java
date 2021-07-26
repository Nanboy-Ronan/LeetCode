import java.lang.Character.Subset;
import java.lang.Thread.State;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums){
        // DFS
        // Time Complexity: O(n*2^n)
        // Space Complexity: O(n*2^n)
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        dfs(nums, 0, new ArrayList<>(), result);
        return result;   
        
    }

    private void dfs(int[] nums, int start_index, List<Integer> subset, List<List<Integer>> result){
        result.add(new ArrayList<>(subset));

        for(int i = start_index; i < nums.length; i++){
            if(i > start_index && nums[i] == nums[i-1]){
                continue;
            }
            subset.add(nums[i]);
            dfs(nums, i+1, subset, result);
            subset.remove(subset.size()-1);
        }
    }
}
