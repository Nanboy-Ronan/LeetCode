# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Hash Set
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        hash_set = set([])
        for num in nums:
            hash_set.add(num)
        for i in range(len(nums)):
            if i not in hash_set:
                return i
        return len(nums)