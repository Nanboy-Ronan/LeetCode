from typing import List


class Solution:
    # DFS
    # Time Complexity: O(mn)
    # Space Complexity: O(mn)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        visitedP = set()
        visitedA = set()

        def dfs(x, y, paths, visited):
            if (x,y) in visited:
                return
            visited.add((x,y))
            for i, j in ((x, y+1), (x+1, y), (x-1, y), (x, y-1)):
                if i >= 0 and i < len(heights) and j >= 0 and j < len(heights[0]):
                    print((x,y))
                    if heights[i][j] >= heights[x][y]:
                        paths.add((i,j))
                        dfs(i, j, paths, visited)

        for i in range(len(heights[0])):
            pacific.add((0, i))
            dfs(0, i, pacific, visitedP)
            atlantic.add((len(heights)-1, i))
            dfs(len(heights)-1, i, atlantic, visitedA)

        for i in range(len(heights)):
            pacific.add((i, 0))
            dfs(i, 0, pacific, visitedP)
            atlantic.add((i, len(heights[0])-1))
            dfs(i, len(heights[0])-1, atlantic, visitedA)

        return pacific & atlantic
                        
############################ Test ########################
soln = Solution()
# print(soln.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(soln.pacificAtlantic([[1,1],[1,1]]))
        