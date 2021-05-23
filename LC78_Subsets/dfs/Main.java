import java.util.ArrayList;
import java.util.List;

public class Main{
    public static void main(String[] args){
        int[] set = {1,2,3};
        System.out.println(subsets(set));
    }

    private static List<List<Integer>> subsets(int[] set){
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        dfs(set, result, 0, subset);
        return result;
    }

    private static void dfs(int[] set, List<List<Integer>> result, int index, List<Integer> subset){
        result.add(new ArrayList<>(subset));
        if(set.length == index) return;
        for(int i = index; i < set.length; i++){ // this determine first element (like starting from 1,2 ...)
            subset.add(set[i]);
            dfs(set, result, i+1, subset);  // this determine the next element (like 1, then 2,3 ...)
            subset.remove(subset.size()-1);
        }
    }
}