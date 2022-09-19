#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
    // BFS
    // Time Complexity: O(m+n)
    // Space Complexity: O(m+n)
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> inDegrees(numCourses, 0); // store the in degree for each node
        vector<vector<int>> neighbours(numCourses); // store nodes neighbour[i] points to

        // Initialize inDegrees and neighbour
        for(vector<int> pre : prerequisites){
            inDegrees[pre[0]]++;
            neighbours[pre[1]].push_back(pre[0]);
        }

        queue<int> queue;

        for(int i = 0; i < inDegrees.size(); i++){
            if(inDegrees[i] == 0){
                queue.push(i);
            }
        }

        int visited = 0;

        while(queue.size() > 0){
            int node = queue.front();
            queue.pop();
            visited++;
            for(int neighbour : neighbours[node]){
                // Decrement in degrees
                inDegrees[neighbour]--;

                if(inDegrees[neighbour] == 0){
                    queue.push(neighbour);
                }
            }
        }

        return numCourses == visited;
        
    }
};