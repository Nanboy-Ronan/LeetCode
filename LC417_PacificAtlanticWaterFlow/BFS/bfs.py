from collections import deque
from typing import List


class Solution:
    # BFS
    # Time Complexity: O(mn)
    # Space Complexity: O(mn)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        queueP = deque()
        queueA = deque()
        n = len(heights)
        m = len(heights[0])
        visitedP = set()
        visitedA = set()
        pacific = set()
        atlantic = set()

        for i in range(n):
            pacific.add((i,0))
            queueP.append((i, 0))
            atlantic.add((i, m-1))
            queueA.append((i,m-1))
        
        for i in range(m):
            pacific.add((0, i))
            queueP.append((0, i))
            atlantic.add((n-1, i))
            queueA.append((n-1, i))

        while len(queueP) > 0:
            length = len(queueP)
            for _ in range(length):
                node = queueP.popleft()
                if (node[0], node[1]) in visitedP:
                    continue
                visitedP.add((node[0], node[1]))
                for x, y in ((node[0]+1, node[1]), (node[0]-1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1)):
                    if x >= 0 and x < n and y >= 0 and y < m:
                        if heights[x][y] >= heights[node[0]][node[1]]:
                            pacific.add((x,y))
                            queueP.append((x,y))
        
        while len(queueA) > 0:
            length = len(queueA)
            for _ in range(length):
                node = queueA.popleft()
                if (node[0], node[1]) in visitedA:
                    continue
                visitedA.add((node[0], node[1]))
                for x, y in ((node[0]+1, node[1]), (node[0]-1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1)):
                    if x >= 0 and x < n and y >= 0 and y < m:
                        if heights[x][y] >= heights[node[0]][node[1]]:
                            atlantic.add((x,y))
                            queueA.append((x,y))
        
        return pacific & atlantic
