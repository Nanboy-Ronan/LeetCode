# Given an array A of N integers, find any 3 elements in it such that A[i] < A[j] < A[k] and i < j < k.
# Input:
# N = 5
# A[] = {1,2,1,1,3}
# Output: 1
# Explanation: a sub-sequence 1 2 3 exist.

# Input:
# N = 3
# A[] = {1,1,3}
# Output: 0
# Explanation: no such sub-sequence exist.

class Solution:
    def find3number(self,A, n):
        if A is None or len(A) < 3:
            return None
        min, max = 0, n-1
        # Create an array to store index of smaller element on the left side
        smaller = [0]*10000
        smaller[0] = -1
        for i in range(1, n):
            if A[i] <= A[min]:
                min = i
                smaller[i] = -1
            else:
                smaller[i] = min
        
        # Create an array to store index of larger element on the right side
        greater = [0]*10000
        greater[n-1] = -1
        for i in range(n-2, -1, -1):
            if A[i] >= A[max]:
                max = i
                greater[i] = -1
            else:
                greater[i] = max
        
        # Find a number which has both a greater number on right side and smaller number on left side
        for i in range(0, n):
            if smaller[i] != -1 and greater[i] != -1:
                print(A[smaller[i]], A[i], A[greater[i]])
        
        print("no such triple found")