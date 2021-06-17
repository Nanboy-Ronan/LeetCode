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

from typing import List


def numIslands(grid: List[List[str]]) -> int:
    result = 0
    if grid is None or len(grid) == 0:
        return result
    
    for i in range(0, len(grid)): # row
        for j in range(0, len(grid[i])): # column
            if grid[i][j] == '1':
                result += 1
                dfs(grid, i, j) # mark all island as '0'
    
    return result

def dfs(grid: List[List[str]], row: int, col: int) -> None:
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]): # check the bound
        return
    
    if grid[row][col] == '0':
        return
    
    grid[row][col] = '0'

    dfs(grid, row-1, col)
    dfs(grid, row+1, col)
    dfs(grid, row, col-1)
    dfs(grid, row, col+1)


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