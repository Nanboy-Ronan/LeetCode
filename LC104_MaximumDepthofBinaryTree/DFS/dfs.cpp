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
    // DFS
    // Time Complexity: O(n)
    // Space Complexity: O(n)
public:
    int maxDepth(TreeNode* root) {
        if(root == nullptr) return 0;
        return dfs(root);
    }

    int dfs(TreeNode* node){
        //Pre
        if(node == nullptr){
            return 0;
        }
        int lLeft = dfs(node->left);
        int lRight = dfs(node->right);
        // Post
        return max(lLeft, lRight) + 1;
    }
};