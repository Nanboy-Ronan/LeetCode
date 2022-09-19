/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    // BFS
    // Time Complexity: O(n)
    // Space Complexity: O(n)
public:
    int maxDepth(TreeNode* root) {
        if(root == nullptr) return 0;
        int result = 0;
        queue<TreeNode*> _queue;
        _queue.push(root);
        while(_queue.size() != 0){
            int levelSize = _queue.size();
            result++;
            for(int i = 0; i < levelSize; i++){
                TreeNode* node = _queue.front();
                _queue.pop();
                if(node->left != nullptr) _queue.push(node->left);
                if(node->right != nullptr) _queue.push(node->right);
            }
        }
        return result;
    }
};