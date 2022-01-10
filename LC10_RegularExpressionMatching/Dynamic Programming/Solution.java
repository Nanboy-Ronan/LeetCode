/*
1. p.charAt(j) == s.charAt(i): dp[i][j] = dp[i-1][j-1]
2. p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1]
3. p.charAt(j) == '*':
    1. p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2] // a* only counts as empty
    2. p.charAt(j-1) == s.charAt(i) or p.charAt(j-1) == '.':
        dp[i][j] = dp[i][j-1] // a* counts as single a
        dp[i][j] = dp[i-1][j] // a* counts as multiple a
        dp[i][j] = dp[i][j-2] // a* counts as empty
*/
class Solution {
    // Dynamic Programming
    // Time Complexity: O(mn)
    // Space Complexity: O(mn)
    public boolean isMatch(String s, String p) {
        if(s == null || p == null){
            return false;
        }
        boolean[][] dp = new boolean[s.length()+1][p.length()+1];
        dp[0][0] = true;
        for(int i = 0; i < p.length(); i++){
            if(p.charAt(i) == '*' && i > 0 && dp[0][i-1]){
                dp[0][i+1] = true;  // "aab" "c*aab"
            }
        }
        for(int i = 0; i < s.length(); i++){
            for(int j = 0; j < p.length(); j++){
                if(p.charAt(j) == s.charAt(i) || p.charAt(j) == '.'){
                    dp[i+1][j+1] = dp[i][j];
                }else if(p.charAt(j) == '*'){
                    if(p.charAt(j-1) != s.charAt(i) && p.charAt(j-1) != '.'){
                        dp[i+1][j+1] = dp[i+1][j-1];
                    }else{
                        dp[i+1][j+1] = (dp[i+1][j] || dp[i][j+1] || dp[i+1][j-1]);
                    }
                }
            }
        }
        return dp[s.length()][p.length()];
    }
}