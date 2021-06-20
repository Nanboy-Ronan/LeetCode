# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

from collections import deque
from typing import List


    
def numIslands(grid: List[List[str]]) -> int:
    # BFS
    # Time Complexity: O(m*n)
    # Space Complexity: O(m*n)
    result = 0
    if grid is None or len(grid) == 0:
        return result
    
    numRow = len(grid)
    numCol = len(grid[0])

    
    for i in range(0,numRow):
        for j in range(0,numCol):
            if grid[i][j] == '1':
                queue = deque([])
                queue.append([i,j])
                grid[i][j] = '0'
                result += 1
            
                while len(queue) != 0:
                    temp = queue.popleft()
                    x = temp[0] # row
                    y = temp[1] # col
                    if isInBound([x-1, y], numRow, numCol):
                        if grid[x-1][y] == '1':
                            grid[x-1][y] = '0'
                            queue.append([x-1,y])
                    if isInBound([x+1, y], numRow, numCol):
                        if grid[x+1][y] == '1':
                            grid[x+1][y] = '0'
                            queue.append([x+1,y])
                    if isInBound([x, y-1], numRow, numCol):
                        if grid[x][y-1] == '1':
                            grid[x][y-1] = '0'
                            queue.append([x,y-1])
                    if isInBound([x, y+1], numRow, numCol):
                        if grid[x][y+1] == '1':
                            grid[x][y+1] = '0'
                            queue.append([x,y+1])
    return result

def isInBound(coordinate: List[int], row: int, col: int) -> bool:
    if coordinate[0] < 0 or coordinate[1] < 0 or coordinate[0] >= row or coordinate[1] >= col:
        return False
    return True


# # # # # # # # # # # # # # # # # # # # Test Cases # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print("test 1: ")
result = numIslands([
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
])
print(result)

print("test 2: ")
result = numIslands([
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
])
print(result)