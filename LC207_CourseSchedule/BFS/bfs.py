from collections import defaultdict, deque
from typing import List


class Solution:
    # BFS
    # Time Complexity: O(m+n)
    # Space Complexity: O(m+n)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # edges[0] is all courses that require 0 as prerequisite
        edges = defaultdict(list)
        indegree = [0]*numCourses

        for pre in prerequisites:
            edges[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
        
        queue = deque()
        # First take course from indegree = 0 (no prerequisite)
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        visited = 0
        while len(queue) > 0:
            node = queue.popleft()
            visited += 1
            # Decrement in degree here
            for n in edges[node]:
                indegree[n] -= 1
                # Add courses with no rerequisite to the queue again
                if indegree[n] == 0:
                    queue.append(n)
        return visited == numCourses
        
########################### Test ######################
soln = Solution()
print(soln.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))  