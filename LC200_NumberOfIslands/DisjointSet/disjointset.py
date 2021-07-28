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
    # Disjoint Set
    # Time Complexity: O(m*n)
    # Space Complexity: O(m*n)
    if grid is None or len(grid) == 0:
        return 0

    row = len(grid)
    col = len(grid[0])
    disjointSet = DisjointSet(grid)
    numWater = 0

    for i in range(0,len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == '0':
                numWater += 1
            elif grid[i][j] == '1':
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for x, y in directions:
                    x = i + x
                    y = j + y
                    if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[i]) and grid[x][y] == '1':
                        disjointSet.union(x*len(grid[i])+y, i*len(grid[i])+j)
                        
    return disjointSet.getNumSet() - numWater



class DisjointSet:
    def __init__(self, grid) -> None:
        row = len(grid)
        col = len(grid[0])
        self.numSet = row*col
        self.root = [-1]*self.numSet
        self.rank = [0]*self.numSet
        for i in range(0, row*col):
            self.root[i] = i # root[x] is the representative
    
    def find(self, x: int) -> int:
        if x == self.root[x]: # represent itself
            return self.root[x]
        else:
            self.root[x] = self.find(self.root[x]) # find with path compression
            return self.root[x]
    
    def union(self, x: int, y: int) -> None:
        repreX = self.find(x)
        repreY = self.find(y)
        if repreX != repreY:
            if self.rank[repreX] > self.rank[repreY]:
                repreX,repreY = repreY,repreX
            self.root[repreX] = repreY
            if self.rank[repreX] == self.rank[repreY]:
                self.rank[repreX] += 1
            self.numSet -= 1
    
    def getNumSet(self) -> int:
        return self.numSet


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