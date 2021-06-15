# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# Input: intervals = [], newInterval = [5,7]
# Output: [[5,7]]
# Input: intervals = [[1,5]], newInterval = [2,3]
# Output: [[1,5]]
# Input: intervals = [[1,5]], newInterval = [2,7]
# Output: [[1,7]]

from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # Brute Force
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    result = []
    index = 0

    # put all intervals with start time smaller than newInterval into the result
    for interval in intervals:
        if interval[0] < newInterval[0]:
            result.append(interval)
            index += 1
        else:
            break
    
    if len(result) == 0: # no intervals or newInterval has the smallest start time
        result.append(newInterval)
    elif result[-1][1] >= newInterval[0]: # newInterval start before the last one (overlap)
        result[-1][1] = max(result[-1][1], newInterval[1])
    else:
        result.append(newInterval)
    
    # continue to copy the rest and merge if necessary
    for i in range(index, len(intervals)):
        if result[-1][1] >= intervals[i][0]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])
    
    return result


# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print("test 1: ")
print(insert([[1,3],[6,9]], [2,5]))

print("test 2: ")
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

print("test 3: ")
print(insert([], [5,7]))

print("test 4: ")
print(insert([[1,5]], [2,3]))

print("test 5: ")
print(insert([[1,5]], [2,7]))