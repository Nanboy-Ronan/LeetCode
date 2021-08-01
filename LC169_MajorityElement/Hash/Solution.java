import java.util.HashMap;

class Solution {
    public int majorityElement(int[] nums) {
        // Hash
        // Time Complexity: O(n)
        // Space Complexity: O(n)
        HashMap<Integer,Integer> mapping = new HashMap<>();

        for(int num: nums){
            if(!mapping.containsKey(num)){
                mapping.put(num, 0);
            }
            mapping.put(num, mapping.get(num)+1);
        }
        int half = nums.length / 2;
        for(int key: mapping.keySet()){
            if(mapping.get(key) > half){
                return key;
            }
        }
        return -1;
    }
}