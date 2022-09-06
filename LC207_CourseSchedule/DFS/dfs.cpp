#include <iostream>
#include <vector>
using namespace std;

class Solution {
    // DFS
    // Time Complexity: O(m+n)
    // Space Complexity: O(m+n)
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // 0 = unvisited 1 = visiting 2= visited
        vector<int> visited(numCourses, 0);
        vector<vector<int>> edges(numCourses); // adjacency list

        for(vector<int> pre : prerequisites){
            edges[pre[1]].push_back(pre[0]);
        }

        for(int i = 0; i < numCourses; i++){
            bool retVal = dfs(i, visited, edges);
            if(!retVal) return false;
        }
        return true;
    }

    bool dfs(int currNode, vector<int> &visited, vector<vector<int>>& edges){
        if(visited[currNode] == 1) return false; // on the path and find a circle
        if(visited[currNode] == 2) return true; // maybe called from outside
        visited[currNode] = 1;
        for(int node : edges[currNode]){
            bool retVal = dfs(node, visited, edges);
            if(!retVal) return false;
        }
        visited[currNode] = 2;
        return true;
    }
};