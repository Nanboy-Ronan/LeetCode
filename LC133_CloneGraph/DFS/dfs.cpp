#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
    // DFS
    // Time Complexity: O(n)
    // Space COmplexity: O(n)
public:
    Node* cloneGraph(Node* node) {
        if(node == nullptr){
            return nullptr;
        }
        unordered_map<int, Node*> visited;
        return dfs(node, visited);
        
    }
    Node* dfs(Node* node, unordered_map<int, Node*>& visited){
        Node* nodeCopy;
        if(visited.count(node->val) == 0){
            nodeCopy = new Node(node->val);
            visited[node->val] = nodeCopy;
        }else{
            nodeCopy = visited[node->val];
            return nodeCopy;
        }

        for(Node* n : node->neighbors){
            if(n != nullptr){
                Node* nCopy = dfs(n, visited);
                nodeCopy->neighbors.push_back(nCopy);
            }
        }
        return nodeCopy;
    }

};