from collections import deque
from typing import List


class Solution:
    # BFS
    # Time Complexity:
    # Space Complexity:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        numRow = len(grid)
        numCol = len(grid[0])
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        result = 0
        for i in range(numRow):
            for j in range(numCol):
                if grid[i][j] == 1:
                    counter = 0
                    queue = deque()
                    queue.append([i,j])
                    while len(queue) > 0:
                        m, n = queue.popleft()
                        grid[m][n] = 0
                        counter += 1
                        for dir in dirs:
                            x = m + dir[0]
                            y = n + dir[1]
                            if x >= 0 and x < numRow and y >= 0 and y < numCol and grid[x][y]:
                                queue.append([x,y])
                    result = result if result >= counter else counter
        return result