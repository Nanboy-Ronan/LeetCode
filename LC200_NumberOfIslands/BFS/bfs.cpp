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
#include <queue>
#include <stdlib.h>
using namespace std;

bool isInBound(pair<int, int> p, int row, int col){
    return p.first >= 0 && p.second >= 0 && p.first < row && p.second < col;
}

int numIslands(vector<vector<char>>& grid){
    // BFS
    // Time Complexity: O(m*n)
    // Space Complexity: O(m*n)
    if(grid.size() == 0){
        return 0;
    }

    int row = grid.size();
    int col = grid[0].size();
    int numIslands = 0;
    vector<vector<char>> gridCopy = grid; // prevent changing the original grid

    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            if(gridCopy[i][j] == '1'){
                gridCopy[i][j] = '0';
                queue<pair<int,int>> queue;
                queue.push({i,j});
                numIslands++;

                while(!queue.empty()){
                    auto temp = queue.front();
                    int x = temp.first;
                    int y = temp.second;
                    queue.pop();
                    if(isInBound({x-1,y},row,col)){
                        if(gridCopy[x-1][y] == '1'){
                            gridCopy[x-1][y] = '0';
                            queue.push({x-1,y});
                        }
                    }
                    if(isInBound({x+1,y},row,col)){
                        if(gridCopy[x+1][y] == '1'){
                            gridCopy[x+1][y] = '0';
                            queue.push({x+1,y});
                        }
                    }
                    if(isInBound({x,y-1},row,col)){
                        if(gridCopy[x][y-1] == '1'){
                            gridCopy[x][y-1] = '0';
                            queue.push({x,y-1});
                        }
                    }
                    if(isInBound({x,y+1},row,col)){
                        if(gridCopy[x][y+1] == '1'){
                            gridCopy[x][y+1] = '0';
                            queue.push({x,y+1});
                        }
                    }
                }
            }
        }
    }

    return numIslands;
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