/*
* Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
* An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
* Input: grid = [
*   ["1","1","1","1","0"],
*   ["1","1","0","1","0"],
*   ["1","1","0","0","0"],
*   ["0","0","0","0","0"]
* ]
* Output: 1
* Input: grid = [
*   ["1","1","0","0","0"],
*   ["1","1","0","0","0"],
*   ["0","0","1","0","0"],
*   ["0","0","0","1","1"]
* ]
* Output: 3
*/
#include <iostream>
#include <vector>
#include <stdlib.h>
using namespace std;

void dfs(vector<vector<char>> &grid, int x, int y){
    if(x < 0 || y < 0 || x >= grid.size() || y >= grid[0].size() ||grid[x][y] == '0') return;
    grid[x][y] = '0';
    dfs(grid, x+1, y);
    dfs(grid, x-1, y);
    dfs(grid, x, y+1);
    dfs(grid, x, y-1);
}


int numIslands(vector<vector<char>>& grid) {
    // DFS
    // Time Complexity: O(m*n)
    // Space Complexity: O(m*n)
    if(grid.size() == 0){
        return 0;
    }

    int row = grid.size();
    int col = grid[0].size();
    int numIsland = 0;
    vector<vector<char>> grid_copy = grid; // prevent changing original grid

    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            if(grid_copy[i][j] == '1'){
                numIsland++;
                dfs(grid_copy, i, j);
            }
        }
    }

    return numIsland;
}


int main(){
    cout << "test 1: " << endl;
    vector<vector<char>> test1 = {
                                    {'1','1','1','1','0'},
                                    {'1','1','0','1','0'},
                                    {'1','1','0','0','0'},
                                    {'0','0','0','0','0'}
                                                            };
    int result = numIslands(test1);
    cout << result << endl;

    cout << "test 2: " << endl;
    vector<vector<char>> test2 = {
                                    {'1','1','0','0','0'},
                                    {'1','1','0','0','0'},
                                    {'0','0','1','0','0'},
                                    {'0','0','0','1','1'}
                                                            };
    result = numIslands(test2);
    cout << result << endl;
    
    return 0;
}