#include <iostream>
#include <vector>
using namespace std;

class Solution {
    // Dynamic Programming
    // Time Complexity: O(n^2)
    // Space Complexity: O(n)
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.size() <= 1){
            return nums.size();
        }

        vector<int> dp(nums.size(), 1);
        dp[0] = 0;
        dp[1] = 1;

        for(int i = 2; i < nums.size(); i++){
            for(int j = 0; j < i; j++){
                if(nums[j] < nums[i]){
                    dp[i] = max(dp[j] + 1, dp[i]);
                }
            }
        }

        return *max_element(begin(dp), end(dp));
    }
};