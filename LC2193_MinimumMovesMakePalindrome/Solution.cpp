// You are given a string s consisting only of lowercase English letters.
// In one move, you can select any two adjacent characters of s and swap them.
// Return the minimum number of moves needed to make s a palindrome.
// Note that the input will be generated such that s can always be converted to a palindrome.

class Solution {
public:
    int minMovesToMakePalindrome(string s) {
        // Greedy Algorithm
        // Time Complexity: O(n^2)
        // Space Complexity: O(1)
        int n = s.size();
        int count = 0; // Number of left-pair characters been processed
        int result = 0;
        for(int i = 0; i< n/2; i++){
            int j = n - 1 - count;
            while(s[j]!=s[i]){
                j--;
            }
            if(i != j){
                int k = n - 1 - count - j;
                result += k;
                while(k--){
                    swap(s[j], s[j+1]);
                    j++;
                }
                count++;
            }
            else{
                // odd element
                int k = n/2 - j;
                result += k;
            }
        }
        return result;
    }
};