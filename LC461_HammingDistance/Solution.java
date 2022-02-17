/*
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.
*/

class Solution {
    public int hammingDistance(int x, int y) {
        int diff = x ^ y;
        int result = 0;
        if(diff == 0){
            return result;
        }
        while(diff != 0){
            int isOne = diff & 1;
            result += isOne;
            diff >>= 1;
        }
        return result;
    }
}