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
    # Memorization
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    mapping = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if n in self.mapping:
                return self.mapping[n]
            else:
                result = self.climbStairs(n-1) + self.climbStairs(n-2)
                self.mapping[n] = result
                return result