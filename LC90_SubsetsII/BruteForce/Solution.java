import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        // Brute Force
        // Time Complexity: O(n*2^n)
        // Space Complxity: O(n*2^n)
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());
        Arrays.sort(nums);
        for(int num : nums){
            int result_size = result.size();
            for(int i = 0; i < result_size; i++){
                List<Integer> temp = new ArrayList<>(result.get(i));
                temp.add(num);
                result.add(temp);
            }
        }
        HashSet<List<Integer>> set = new HashSet<>(result);
        return new ArrayList<>(set);
    }
}