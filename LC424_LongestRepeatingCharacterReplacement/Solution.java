class Solution {
    // Sliding Window
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int characterReplacement(String s, int k) {
        int len = s.length();
        if(len < 2){
            return len;
        }
        char[] charArray = s.toCharArray();
        int[] freq = new int[26];
        int maxCount = 0;

        // [left, right)
        int left = 0;
        int right = 0;
        int result;
        while(right < len){
            freq[charArray[right] - 'A']++;
            maxCount = Math.max(maxCount, freq[charArray[right] - 'A']);
            right++;

            if(right - left > maxCount + k){
                freq[charArray[left] - 'A']--;
                left++;
            }
            result = Math.max(result, right - left);
        }
        return result;  
    }
}