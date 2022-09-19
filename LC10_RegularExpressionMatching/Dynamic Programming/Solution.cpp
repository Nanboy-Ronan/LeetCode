#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        // Dynamic Programming
        // Time Complexty: O(mn)
        // Space Complexity: O(mn)
        vector<vector<bool>> dp(s.length() + 1, vector<bool>(p.length() + 1));
        dp[0][0] = true;
        return false;
    }
};