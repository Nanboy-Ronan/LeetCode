from typing import List


class Solution:
    # Traverse
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        preProduct = [0]*n
        postProduct = [0]*n
        
        preProduct[0] = 1
        for i in range(1, len(nums)):
            preProduct[i] = preProduct[i-1]*nums[i-1]
        
        postProduct[-1] = 1
        for i in reversed(range(len(nums)-1)):
            postProduct[i] = postProduct[i+1]*nums[i+1]

        for i in range(len(nums)):
            result.append(preProduct[i]*postProduct[i])
        
        return result

#################################### Test ###############################
soln = Solution()
print(soln.productExceptSelf([1,2,3,4]))