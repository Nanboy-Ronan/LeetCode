import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class BackTrack {
    public List<List<Integer>> permute(int[] nums) {
        if(nums.length == 0) return new ArrayList<>(new ArrayList<>());
        List<List<Integer>> result = new ArrayList<>();
        HashMap<Integer,Boolean> visited = new HashMap<>();

        for(int num : nums){
            visited.put(num, false);
        }

        backTrack(nums, visited, new ArrayList<>(), result);

        return result;
        
    }

    private void backTrack(int[] nums, HashMap<Integer,Boolean> visited, List<Integer> subset, List<List<Integer>> result){
        if(subset.size() == nums.length){
            result.add(new ArrayList<>(subset));
            return;
        }

        for(int num : nums){
            if(!visited.get(num)){
                subset.add(num);
                visited.put(num, true);
                backTrack(nums, visited, subset, result);
                visited.put(subset.get(subset.size()-1), false);
                subset.remove(subset.size()-1);
            }
        }
    }
}