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

class DisjointSet{
public:
    DisjointSet(vector<vector<char>> & grid){
        int row = grid.size();
        int col = grid[0].size();
        numSet = row * col;
        for(int i = 0; i < numSet; i++){
            root.push_back(i);
            rank.push_back(0);
        }
    }

    int find(int x){
        if(x == root[x]) return root[x];
        else{
            root[x] = find(root[x]);
            return root[x];
        }
    }

    void unite(int x, int y){
        int repreX = find(x);
        int repreY = find(y);

        if (repreX != repreY){
            if(rank[repreX] > rank[repreY]){
                swap(repreX,repreY);
            }
            root[repreX] = repreY;
            if(rank[repreX] == rank[repreY]){
                rank[repreX] += 1;
            }
            numSet--;
        }
    }

    int getNumSet() const{
        return numSet;
    }

private:
    vector<int> root;
    vector<int> rank;
    int numSet;
};

int numIslands(vector<vector<char>>& grid) {
    // Disjoint Set
    // Time Complexity: O(m*n)
    // Space Complexity: O(m*n)
    if(grid.size() == 0) return 0;

    DisjointSet disjointSet(grid);
    int row = grid.size();
    int col = grid[0].size();
    int numWater = 0;

    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            if(grid[i][j] == '0') numWater++;
            else if(grid[i][j] == '1'){
                vector<pair<int,int>> directions = {{0,1},{0,-1},{1,0},{-1,0}};
                for(pair<int,int> direction : directions){
                    int x = i + direction.first;
                    int y = j + direction.second;
                    if(x >= 0 && y >= 0 && x < row && y < col && grid[x][y] == '1'){
                        disjointSet.unite(i*row+j, x*row+y);
                    }
                }
            }
        }
    }

    return disjointSet.getNumSet() - numWater;
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