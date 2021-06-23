# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return the nth ugly number.
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

import heapq

def nthUglyNumber(n: int) -> int:
    # Min Heap and HashSet
    # Time Compleity: O(nlogn)
    # Space Complexity: O(n)
    hashSet = set()
    heap = []
    result = 1

    hashSet.add(1)
    heapq.heappush(heap, 1)
    factors = (2,3,5)

    for i in range(n):
        result = heapq.heappop(heap)
        for factor in factors:
            newNum = result * factor
            if newNum not in hashSet:
                hashSet.add(newNum)
                heapq.heappush(heap, newNum)
    return result


# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print("test 1: ")
print(nthUglyNumber(10)) # expect 12

print("test 2: ")
print(nthUglyNumber(1)) # expect 1