/*
// Definition for a Node.
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
*/

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
public:
    // BFS
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    Node* cloneGraph(Node* node) {
        if(node == nullptr) return nullptr;
        unordered_map<int, Node*> visited;
        queue<Node*> _queue;

        _queue.push(node);
        Node* root = new Node(node->val);
        visited[root->val] = root;

        while(_queue.size() != 0){
            int levelLength = _queue.size();
            for(int i = 0; i < levelLength; i++){
                Node* n = _queue.front();
                _queue.pop();

                for(Node* neighbor : n->neighbors){
                    if(visited.count(neighbor->val) == 0){
                        Node* nodeCopy = new Node(neighbor->val);
                        visited[nodeCopy->val] = nodeCopy;
                        _queue.push(neighbor);
                    }
                    visited[n->val]->neighbors.push_back(visited[neighbor->val]);
                }
            }
        }

        return root;

    }
};