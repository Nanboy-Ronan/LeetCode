import java.util.HashMap;

class Solution {
    // Traverse
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int romanToInt(String s) {
        if(s == null || s.length() == 0){
            return 0;
        }
        // construct the map
        HashMap<Character,Integer> mapping = new HashMap<>();
        mapping.put('I', 1);
        mapping.put('V', 5);
        mapping.put('X', 10);
        mapping.put('L', 50);
        mapping.put('C', 100);
        mapping.put('D', 500);
        mapping.put('M', 1000);

        // convert result
        int result = mapping.get(s.charAt(0));
        for(int i = 1; i < s.length(); i++){
            if(mapping.get(s.charAt(i)) > mapping.get(s.charAt(i-1))){
                result += mapping.get(s.charAt(i)) - 2*mapping.get(s.charAt(i-1));
            }else{
                result += mapping.get(s.charAt(i));
            }
        }
        return result;
        
    }
}