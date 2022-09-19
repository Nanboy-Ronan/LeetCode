from typing import List


class Solution:
    # One time Traversal
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxPrifit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxPrifit = max(maxPrifit, price-minPrice)
        return maxPrifit
