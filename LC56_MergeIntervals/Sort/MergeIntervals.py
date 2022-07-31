# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    # Sort
    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals

    # sort the interval accoding to the first elements of every sublist
    intervals.sort(key = lambda x: x[0])

    result = []

    for interval in intervals:
        if len(result) == 0:
            result.append(interval)
        elif interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    
    return result


# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print("test 1: ")
print(merge([[1,3],[2,6],[8,10],[15,18]])) # Expect [[1, 6], [8, 10], [15, 18]]

print("test 2: ")
print(merge([[15,18], [8,10], [2,6], [1,3]])) # Expect [[1, 6], [8, 10], [15, 18]]

print("test 3: ")
print(merge([[1,4],[4,5]])) # Expect [[1, 5]]