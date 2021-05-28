/*
* Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
* Input: root = [3,9,20,null,null,15,7]
* Output: [[3],[9,20],[15,7]]
* Input: root = [1]
* Output: [[1]]
* Input: root = []
* Output: []
*/
#include <iostream>
#include <stdlib.h>
#include <vector>
using namespace std;

struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(): val(0), left(nullptr), right(nullptr){}
    TreeNode(int x): val(x), left(nullptr), right(nullptr){}
    TreeNode(int x, TreeNode *left, TreeNode *right): val(x), left(left), right(right){}
};

void dfs(TreeNode* node, vector<vector<int>> &result, int level){
    if(node == nullptr) return;

    if(level > ((int)result.size()-1)){
        result.push_back(vector<int>());
    } 
    result[level].push_back(node->val);

    dfs(node->left, result, level+1);
    dfs(node->right, result, level+1);
}

vector<vector<int>> levelOrder(TreeNode* root){
    vector<vector<int>> result;

    if(root == nullptr) return result;

    dfs(root, result, 0);
    
    return result;
}



int main(){
    TreeNode* root1 = new TreeNode(3);
    root1->left = new TreeNode(9);
    root1->right = new TreeNode(20);
    root1->right->left = new TreeNode(15);
    root1->right->right = new TreeNode(7);
    vector<vector<int>> result = levelOrder(root1);
    for(auto row_obj : result){
        for(auto elem: row_obj){
             cout << elem << ", ";
        }
        cout << endl;
    }
    cout << endl;

    TreeNode* root2 = new TreeNode(1);
    result = levelOrder(root2);
    for(auto row_obj : result){
        for(auto elem: row_obj){
             cout << elem << ", ";
        }
        cout << endl;
    }
    cout << endl;

    TreeNode* root3 = nullptr;
    result = levelOrder(root3);
    for(auto rowObj : result){
        for(auto elem: rowObj){
             cout << elem << ", ";
        }
        cout << endl;
    }
    cout << endl;

    
}