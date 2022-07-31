/*
* Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
* Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
* Output: [[1,6],[8,10],[15,18]]
* Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
* Input: intervals = [[1,4],[4,5]]
* Output: [[1,5]]
* Explanation: Intervals [1,4] and [4,5] are considered overlapping.
*/

#include <iostream>
#include <stdlib.h>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(vector<int> a, vector<int> b){
    return a[0] < b[0];
}

vector<vector<int>> merge(vector<vector<int>>& intervals) {
    // Sort
    // Time Complexity: O(nlogn)
    // Space Complexity: O(1)
    sort(intervals.begin(), intervals.end(), cmp);

    vector<vector<int>> result;

    for(auto interval : intervals){
        if(result.empty()){
            result.push_back(interval);
        }else if(result.back()[1] >= interval[0]){
            result.back()[1] = max(result.back()[1], interval[1]);
        }else{
            result.push_back(interval);
        }
    }

    return result;
}

int main(){
    // test 1
    cout << "test 1: " << endl;
    vector<vector<int>> test1{{1,3},{2,6},{8,10},{15,18}};
    vector<vector<int>> result = merge(test1); // Expect [[1, 6], [8, 10], [15, 18]]
    for(int i = 0; i<result.size(); i++){
        cout << "[";
        for(int j=0; j < result[0].size(); j++){
            cout << result[i][j] << ", ";
        }
        cout << "]" << endl;
    }

    // test 2
    cout << "test 2: " << endl;
    vector<vector<int>> test2{{15,18},{8,10},{2,6},{1,3}};
    result = merge(test2); // Expect [[1, 6], [8, 10], [15, 18]]
    for(int i = 0; i<result.size(); i++){
        cout << "[";
        for(int j=0; j < result[0].size(); j++){
            cout << result[i][j] << ", ";
        }
        cout << "]" << endl;
    }
    
    // test 3
    cout << "test 3: " << endl;
    vector<vector<int>> test3{{1,4},{4,5}};
    result = merge(test3); // Expect [[1, 5]]
    for(int i = 0; i<result.size(); i++){
        cout << "[";
        for(int j=0; j < result[0].size(); j++){
            cout << result[i][j] << ", ";
        }
        cout << "]" << endl;
    }
    return 0;
}