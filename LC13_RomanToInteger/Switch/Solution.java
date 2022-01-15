/*
Pattern: left < right then right - left, otherwise reverse.
*/
class Solution {
    // Traverse
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int romanToInt(String s) {
        if(s==null || s.length() == 0){
            return 0;
        }

        int result = toInt(s.charAt(0));
        for(int i = 1; i < s.length(); i++){
            if(toInt(s.charAt(i)) > toInt(s.charAt(i - 1))){
                // pattern: right - left
                // time 2 because in the else we added the left previously so minus it
                result += toInt(s.charAt(i)) - 2*toInt(s.charAt(i - 1));
            }else{
                result += toInt(s.charAt(i));
            }
        }
        

        return result;
    }

    public int toInt(char c){
        int result = 0;
        switch(c){
            case 'I' : return 1;
            case 'V' : return 5;
            case 'X' : return 10;
            case 'L' : return 50;
            case 'C' : return 100;
            case 'D' : return 500;
            case 'M' : return 1000;
        }
        return result;
    }
}