import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
 * LeetCode 78 Subsets Given an integer array nums of unique elements, return
 * all possible subsets (the power set). The solution set must not contain
 * duplicate subsets. Return the solution in any order. Input: nums = [1,2,3]
 * Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 */

public class Main{
     /*
     * brute force
     * Time Complexity: O(n*2^n)
     * Space Complexity: O(n*2^n)
     */
    public static void main(String[] args){
        Integer[] set = {1,2,3};
        List<Integer> sets = Arrays.asList(set);
        List<List<Integer>> result = subsets(sets);
        System.out.println(result);
     }

    /*
    * This function will return the subsets given the originally set.
    * @param set is the input set that we want to find the subsets on it.
    *
    */
     private static List<List<Integer>> subsets(List<Integer> set){
         List<List<Integer>> result = new ArrayList<>();
         result.add(new ArrayList<>()); // we start with an empty set (empty set is a subset of any set)
         for(int num : set){
             List<List<Integer>> temp = new ArrayList<>(); //temp hold all the subsets after adding the next number
            for(List<Integer> subset : result){
                List<Integer> copy = new ArrayList<>(subset);
                copy.add(num);
                temp.add(copy);
             }
             result.addAll(temp);
         }
         
         return result;

     }
}