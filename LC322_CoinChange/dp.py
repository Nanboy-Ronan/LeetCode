from typing import List


class Solution:
    # Dynamic Programming
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0 and amount != 0:
            return -1
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                else:
                    dp[i] = min(1+dp[i-coin], dp[i])

        return dp[amount] if dp[amount] != amount + 1 else -1
