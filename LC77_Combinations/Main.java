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
        String toPrint = result.toString();
        System.out.println(toPrint);
    }

    private static List<List<Integer>> combine(int n, int k){
        List<List<Integer>> result = new ArrayList<>();
        backtracking(n, k, result, 1, new ArrayList<>());
        return result;
    }

    private static void backtracking(int n, int k, List<List<Integer>> result, int begin, ArrayList<Integer> list){
        if(list.size() == k){
            result.add(new ArrayList<>(list));
            return;
        }

        for(int i = begin; i <= n; i++){
            list.add(i);
            backtracking(n, k, result, i+1, list);
            list.remove(list.size()-1);
        }
    }
}