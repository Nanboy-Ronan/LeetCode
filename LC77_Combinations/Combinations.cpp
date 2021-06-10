/* LeetCode 77. Combinations
    Given two integers n and k, return all possible combinations of k numbers out of the range [1, n]. You may return the answer in any order.
    Methond: Backtracking
    Time Complexity: O(c(n,k))
    Space Complxity: O(k)
*/

Input: n = 1, k = 1
Output: [[1]]
*/
#include <iostream>
#include <stdlib.h>
#include <vector>
using namespace std;

void backTracking(int begin, int end, int k, vector<vector<int>> &result, vector<int> &subset){
    if(subset.size() == k){
        result.push_back(subset);
        return;
    }

    for(int i = begin; i <= end; i++){
        subset.push_back(i);
        backTracking(i + 1, end, k, result, subset);
        subset.pop_back();
    }
}

vector<vector<int>> combine(int n, int k){
    vector<vector<int>> result;
    vector<int> subset;
    backTracking(1, n, k, result, subset);
    return result;
}

int main(){
    vector<vector<int>> result;
    result = combine(4,2);
    for(int i = 0; i<result.size(); i++){
        cout << "[";
        for(int j=0; j < result[0].size(); j++){
            cout << result[i][j] << ", ";
        }
        cout << "]" << endl;
    }
        
}