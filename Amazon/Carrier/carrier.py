# You are an amazon delivery and you have some boxes that you have to deliver, but there are some conditions -

# You can take 2 boxes of same weight in one round
# you can take 3 boxes of same weight in one round
# You have to find the minimum number of rounds to deliver the boxes or -1 if it is not possible to deliver them.

# Example cases -
# Input: boxes - [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
# Output: 4
# Explanation: 3 boxes of weight 2 in 1st round, 2 boxes of weight 3 in 2nd round, 3 boxes of wt 4 in 3rd and 2 boxes of wt 4 in 4th round.

# Input: boxes - [2, 3, 3]
# Output: -1
# Explanation: There is only one box with weight 2 and we can only take either 2 or 3 boxes in one round not lesser.

from collections import Counter
import math
def boxes(weights):
    # Dynamic Programming
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    f = [-1,1,1]
    # f.append(0)
    def dp(num):
        for i in range(1,num+1):
            cost = math.inf
            if i - 2 >= 0:
                cost = min(cost, f[i-1]+1)
            if i - 3 >= 0:
                cost = min(cost, f[i-3]+1)
            f.append(cost)
        return f[num-1]

    count = Counter(weights)
    ans = 0
    for k, v in count.items():
        temp = dp(v)
        if temp == -1:
            return -1
        ans += dp(v)
    return ans

########################## Test ##########################
print(boxes([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
print(boxes([2, 3, 3]))