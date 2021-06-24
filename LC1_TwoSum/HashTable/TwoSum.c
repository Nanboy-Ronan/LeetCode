/*
* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
* You may assume that each input would have exactly one solution, and you may not use the same element twice.
* You can return the answer in any order.

* Input: nums = [2,7,11,15], target = 9
* Output: [0,1]
* Output: Because nums[0] + nums[1] == 9, we return [0, 1].
* Input: nums = [3,2,4], target = 6
* Output: [1,2]
* Input: nums = [3,3], target = 6
* Output: [0,1]
*/

#include <stdio.h>
#include <stdlib.h>
#include "hashInteger.h"

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    // Hash
    // Time Complexity: O(n)
    // Space Complxity: O(n)
    int* result = malloc(sizeof(int)*2);

    Table* hashMap = hashTableInit();
    for(int i = 0; i < numsSize; i++){
        hashPut(hashMap, nums[i], i);
    }
    
    for(int i = 0; i < numsSize; i++){
        int diff = target - nums[i];
        if(hashGet(hashMap,diff) != NULL && hashGet(hashMap,diff) != i){
            result[0] = nums[i];
            result[1] = diff;
            *returnSize = 2;
            return result;
        }
    }

    returnSize = 0;
    return NULL;
}


int main(){
    printf("test 1: \n");
    int* test1 = malloc(4*sizeof(int));
    test1[0] = 2;test1[1] = 7;test1[2] = 11;test1[3] = 15;
    int* returnSize1 = malloc(sizeof(int));
    int* result1;
    result1 = twoSum(test1,4,9,returnSize1);
    printf("First: %d\n",result1[0]);
    printf("Second: %d\n",result1[1]);
    printf("Return Size: %d\n",*returnSize1);

    printf("test 2: \n");
    int* test2 = malloc(3*sizeof(int));
    test2[0] = 3;test2[1] = 2;test2[2] = 4;
    int* returnSize2 = malloc(sizeof(int));
    int* result2;
    result2 = twoSum(test2,3,6,returnSize2);
    printf("First: %d\n",result2[0]);
    printf("Second: %d\n",result2[1]);
    printf("Return Size: %d\n",*returnSize2);

    printf("test 3: \n");
    int* test3 = malloc(2*sizeof(int));
    test3[0] = 3;test3[1] = 3;
    int* returnSize3 = malloc(sizeof(int));
    int* result3;
    result3 = twoSum(test3,3,6,returnSize3);
    printf("First: %d\n",result3[0]);
    printf("Second: %d\n",result3[1]);
    printf("Return Size: %d\n",*returnSize3);
}