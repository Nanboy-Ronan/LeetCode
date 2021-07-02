/*
* Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
* You must write an algorithm with O(log n) runtime complexity.
* Input: nums = [1,3,5,6], target = 5
* Output: 2
* Input: nums = [1,3,5,6], target = 2
* Output: 1
* Input: nums = [1,3,5,6], target = 7
* Output: 4
* Input: nums = [1,3,5,6], target = 0
* Output: 0
* Input: nums = [1], target = 0
* Output: 0
*/

#include <iostream>
#include <stdlib.h>
#include <vector>
using namespace std;

int searchInsert(vector<int>& nums, int target){
    if(nums.size() == 0) return 0;

    int left = 0;
    int right = nums.size() - 1;

    while(left < right){
        int mid = right - (right - left) / 2;
        if(nums[mid] == target) return mid;
        else if(nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }

    return nums[left] > target? left : left + 1;
}


int main(){
    cout << "test 1: " << endl;
    vector<int> list1 = {1,3,5,6};
    cout << searchInsert(list1, 5) << endl;

    cout << "test 2: " << endl;
    cout << searchInsert(list1, 2) << endl;

    cout << "test 3: " << endl;
    cout << searchInsert(list1, 7) << endl;

    cout << "test 4: " << endl;
    cout << searchInsert(list1, 0) << endl;

    cout << "test 5: " << endl;
    vector<int> list2 = {1};
    cout << searchInsert(list2, 0) << endl;

    return 0;
}