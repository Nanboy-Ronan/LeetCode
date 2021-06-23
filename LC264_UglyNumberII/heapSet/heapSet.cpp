/*
* An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
* Given an integer n, return the nth ugly number.
* Input: n = 10
* Output: 12
* Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
* Input: n = 1
* Output: 1
* Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
*/

#include <iostream>
#include <stdlib.h>
#include <unordered_set>
#include <queue>
#include <vector>
using namespace std;

int nthUglyNumber(int n) {
    unordered_set<int> set;
    priority_queue<int, vector<int>, greater<int>> minHeap;

    vector<int> factors = {2,3,5};
    int result = 1;
    set.insert(1);
    minHeap.push(1);

    for(int i = 0; i < n; i++){
        result = minHeap.top();
        minHeap.pop();
        for(int factor : factors){
            int newNum = result * factor;
            if(!set.count(newNum)){
                set.insert(newNum);
                minHeap.push(newNum);
            }
        }
    }

    return result;
}


int main(){
    cout << "test 1: " << endl;
    cout << nthUglyNumber(10) << endl; // expected 12

    cout << "test 2: " << endl;
    cout << nthUglyNumber(1) << endl; // expected 1

    return 0;
}