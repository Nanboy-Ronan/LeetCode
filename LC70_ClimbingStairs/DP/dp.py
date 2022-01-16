'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

'''
Idea:
f(n) = 1 if n = 1
f(n) = 2 if n = 2
f(n) = f(n-1) + f(n-2)
'''

class Solution:
    # Dynamic Programming
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        result = 0
        prePre = 1
        pre = 2 # for 3
        for i in range(3, n+1):
            result = pre + prePre
            prePre = pre
            pre = result
        return result

######################################## Test ###########################################
test = Solution()
print(test.climbStairs(3))
            
