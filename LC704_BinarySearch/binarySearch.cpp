/*
* Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
* You must write an algorithm with O(log n) runtime complexity.
* Input: nums = [-1,0,3,5,9,12], target = 9
* Output: 4
* Explanation: 9 exists in nums and its index is 4
* Input: nums = [-1,0,3,5,9,12], target = 2
* Output: -1
* Explanation: 2 does not exist in nums so return -1
*/

#include <iostream>
#include <stdlib.h>
#include <vector>
using namespace std;

int search(vector<int>& nums, int target){
    if (nums.size() == 0) return -1;

    int left = 0;
    int right = nums.size() - 1;

    while(left <= right){
        int mid = right - (right - left) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else if (nums[mid] > target) right = mid - 1;
    }

    return -1;
}

int main(){
    int t1[] = {-1,0,3,5,9,12};
    vector<int> test1(t1, t1 + sizeof(t1)/sizeof(int));
    cout<< "test1: " << endl;
    cout<< search(test1, 9) << endl; // 4

    int t2[] = {-1,0,3,5,9,12,13};
    vector<int> test2(t2, t2 + sizeof(t2)/sizeof(int));
    cout<< "test1: " << endl;
    cout<< search(test2, 13) << endl; // 6

    int t3[] = {-1,0,3,5,9,12};
    vector<int> test3(t3, t3 + sizeof(t3)/sizeof(int));
    cout<< "test1: " << endl;
    cout<< search(test3, 2) << endl; // -1
}