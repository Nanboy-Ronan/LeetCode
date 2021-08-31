import java.util.HashSet;

class Solution {
    public int missingNumber(int[] nums) {
        // Hash Set
        // Time Complxity: O(n)
        // Space Complexity: O(n)
        HashSet<Integer> hash_set = new HashSet<>();
        for(int num : nums){
            hash_set.add(num);
        }
        for(int i = 0; i < nums.length; i++){
            if(!hash_set.contains(i)){
                return i;
            }
        }
        return nums.length;
    }
}