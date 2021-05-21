import java.util.ArrayList;
import java.util.List;

/*
 * LeetCode 78 Subsets Given an integer array nums of unique elements, return
 * all possible subsets (the power set). The solution set must not contain
 * duplicate subsets. Return the solution in any order. Input: nums = [1,2,3]
 * Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 */

public class Main {
    /*
     * backtracking Time Complexity: O(n*2^n) Space Complexity: O(n*2^n)
     */

    public static void main(String[] args) {
        int[] set = { 1, 2, 3 };
        List<List<Integer>> result = subsets(set);
        System.out.println(result);
    }

    /*
    * This function will return the subsets given the originally set.
    * @param set is the input set that we want to find the subsets on it.
    *
    */
    private static List<List<Integer>> subsets(int [] set){
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());
        for(int i = 1; i <= set.length; i++){
            backtracking(set, result, i, 0, new ArrayList<>());
        }
        return result;
    }

    private static void backtracking(int[] set, List<List<Integer>> result, int length, int index, List<Integer> subset){
        if(subset.size() == length){
            result.add(new ArrayList<>(subset));
            return;
        }
        
        for(int i = index; i < set.length; i++){
            subset.add(set[i]);
            backtracking(set, result, length, i+1, subset); // it will track and add all subset in this route until stop and return
            subset.remove(subset.size()-1); // return back to previous level
        }
    }

}