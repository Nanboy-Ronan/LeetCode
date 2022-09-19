#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Hash Table
        // Time Complexty: O(n)
        // Space Complexty: O(n)
        unordered_map<int, int> mapping;

        for(int i = 0; i < nums.size(); i++){
            mapping[nums[i]] = i;
        }

        vector<int> result;
        for(int i = 0; i < nums.size(); i++){
            if(mapping.count(target - nums[i]) == 1 && mapping[target - nums[i]] != i){
                result.push_back(i);
                result.push_back(mapping[target - nums[i]]);
                break;
            }
        }

        return result;
    }
};