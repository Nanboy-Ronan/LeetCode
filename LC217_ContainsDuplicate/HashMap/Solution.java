import java.util.HashMap;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Hash Map
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        if(nums.length == 0){
            return false;
        }

        HashMap<Integer,Integer> hashMap = new HashMap<>();
        for(int num : nums){
            if(!hashMap.containsKey(num)){
                hashMap.put(num, 0);
            }
            hashMap.put(num, hashMap.get(num)+1);
        }
        for(int value : hashMap.values()){
            if(value > 1)
            return true;
        }
        return  false;
    }
}