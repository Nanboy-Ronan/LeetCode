import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Hash Set
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        if(nums.length == 0){
            return false;
        }
        
        HashSet<Integer> hashSet = new HashSet<>();

        for(int num : nums){
            hashSet.add(num);
        }

        return hashSet.size() == nums.length? false : true;
    }
}