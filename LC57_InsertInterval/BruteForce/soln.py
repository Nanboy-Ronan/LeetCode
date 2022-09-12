from typing import List


class Solution:
    # Traverse
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = newInterval[0]
        right = newInterval[1]
        result = []
        placed = False

        for interval in intervals:
            if interval[0] > right:
                # xxx new interval xxx
                if not placed:
                    result.append([left, right])
                    placed = True
                result.append(interval)
            elif interval[1] < left:
                # xxx interval new xxx
                result.append(interval)
            else:
                # intersection
                left = min(left, interval[0])
                right = max(right, interval[1])
        
        if not placed:
            result.append([left, right])
        
        return result
