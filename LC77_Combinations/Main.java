import java.util.ArrayList;
import java.util.List;

public class Main{
    /* LeetCode 77. Combinations
       Given two integers n and k, return all possible combinations of k numbers out of the range [1, n]. You may return the answer in any order.
       Methond: Backtracking
       Time Complexity: O(c(n,k))
       Space Complxity: O(k)
    */
    public static void main(String[] args){
        List<List<Integer>> result = new ArrayList<>();
        result = combine(4, 2);
        //String toPrint = result.toString();
        System.out.println(result);
    }

    /*
    * This function will return the combinations (with elements of k) in array of [1,n].
    * @param n is the last number (to stop) starting from 1 and ranging from [1,n].
    * @param k is the number required in each combination.
    */
    private static List<List<Integer>> combine(int n, int k){
        List<List<Integer>> result = new ArrayList<>();
        backTracking(n, k, result, 1, new ArrayList<>());
        return result;
    }

    /*
    * This function will help back track combinations. We dismiss the current number before nature recurrtion to avoid duplicate
    * combinations.
    * @param n is the last number (to stop) starting from 1 and ranging from [1,n].
    * @param k is the number required in each combination.
    * @param result is the result for the hole question. This function will modify result and pass it back.
    * @param begin is the start to backtack. We add one to begin for every backtrack to avoid dduplicate combinationos.
    * @param list contains all the combination with the current number (combination so far).
    *
    */
    private static void backTracking(int n, int k, List<List<Integer>> result, int begin, ArrayList<Integer> list){
        if(list.size() == k){
            /* return if we reach the list size */
            result.add(new ArrayList<>(list));  // here we need to copy the list to avoid later change of the list
            return;
        }

        for(int i = begin; i <= n; i++){
            list.add(i);
            backTracking(n, k, result, i+1, list);
            list.remove(list.size()-1);
        }
    }
}