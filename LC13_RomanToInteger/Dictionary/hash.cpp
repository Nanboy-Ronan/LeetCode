#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        // Iteration
        // Time Complexity: O(1)
        // Space Complexity: O(1)
        unordered_map<char, int> mapping {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}
            };
        if(s.length() == 0){
            return 0;
        }
        int result = mapping[s[0]];
        for(int i = 1; i < s.length(); i++){
            if(mapping[s[i]] > mapping[s[i-1]]){
                result = result + mapping[s[i]] - 2*mapping[s[i-1]];
            }else{
                result += mapping[s[i]];
            }
        }
        return result;
    }
};