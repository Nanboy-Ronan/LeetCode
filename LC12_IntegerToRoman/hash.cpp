#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
private:
    vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> strs = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

public:
    string intToRoman(int num) {
        // Traverse
        // Time Complexity: O(1)
        // Space Complexity: O(1)
        string result = "";
        for(int i = 0; i < values.size(); i++){
            while(num >= values[i]){
                if(num >= values[i]){
                    result += strs[i];
                    num -= values[i];
                }
            }
        }
        return result;
    }
};