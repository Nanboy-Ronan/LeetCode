#include <iostream>
#include <stdlib.h>
#include <vector>
#include <queue>
using namespace std;

struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(): val(0), left(nullptr), right(nullptr){}
    TreeNode(int x): val(x), left(nullptr), right(nullptr){}
    TreeNode(int x, TreeNode *left, TreeNode *right): val(x), left(left), right(right){}
};

vector<vector<int>> levelOrder(TreeNode* root){
    vector<vector<int>> result;

    if(root == nullptr) return result;

    // BFS
    queue<TreeNode*> queue;
    queue.push(root);
    while(!queue.empty()){
        size_t size = queue.size();
        vector<int> list;
        while(size != 0){
            TreeNode* curr = queue.front();
            queue.pop();
            list.push_back(curr->val);
            // add the children
            if(curr->left != nullptr) queue.push(curr->left);
            if(curr->right != nullptr) queue.push(curr->right);
            size--;
        }
        result.push_back(list);
    }
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