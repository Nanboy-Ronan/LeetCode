#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // Dynamic Programming
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    int coinChange(vector<int>& coins, int amount) {
        if(coins.size() == 0 && amount != 0){
            return -1;
        }
        vector<int> dp(amount+1, amount+1);
        dp[0] = 0;

        for(int i = 1; i < dp.size(); i++){
            for(int coin : coins){
                if(i - coin >= 0){
                    dp[i] = min(dp[i], 1+dp[i-coin]);
                }
            }
        }

        if(dp[amount] == amount+1){
            // There is no suitable combinations
            return -1;
        }
        return dp[amount];
    }
};