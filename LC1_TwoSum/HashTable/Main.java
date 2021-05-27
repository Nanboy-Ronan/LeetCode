import java.util.Arrays;
import java.util.HashMap;

/*
* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
* You may assume that each input would have exactly one solution, and you may not use the same element twice.
* You can return the answer in any order.

* Input: nums = [2,7,11,15], target = 9
* Output: [0,1]
* Output: Because nums[0] + nums[1] == 9, we return [0, 1].
* Input: nums = [3,2,4], target = 6
* Output: [1,2]
* Input: nums = [3,3], target = 6
* Output: [0,1]
*/

public class Main{
    /*
    * Hash Table
    * Time Complexity: O(n)
    * Space Complexity: O(n)
    */
    public static void main(String[] args){
        int[] test1 =  {2,7,11,15};
        int[] test2 =  {3,2,4};
        int[] test3 =  {3,3};
        System.out.println(Arrays.toString(twoSum(test1, 9)));
        System.out.println(Arrays.toString(twoSum(test2, 6)));
        System.out.println(Arrays.toString(twoSum(test3, 6)));
    }

    private static int[] twoSum(int[] nums, int target){
        int[] result = new int[2];
        HashMap<Integer, Integer> hashTable = new HashMap<>();
        for(int i = 0; i <= nums.length - 1; i++){
            hashTable.put(nums[i], i);
        }
        for(int i = 0; i <= nums.length - 1; i++){
            int diff = target - nums[i];
            if(hashTable.containsKey(diff) && hashTable.get(diff)!= i){
                result[0] = i;
                result[1] = hashTable.get(diff);
            }
        }
        return result;
    }
}