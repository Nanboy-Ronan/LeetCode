/*
* Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
* Input: n = 3
* Output: ["((()))","(()())","(())()","()(())","()()()"]
* Input: n = 1
* Output: ["()"]
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print(char* str){
    while(*str != '\0'){
       printf("%c",*str++); 
    }
}


void backTrack(int n, char** result, char* subset, int left, int right, int* resultSize, int* subsetSize){
    if(left < right || left > n || right > n) return;
    if(right == n && left == n){
        *resultSize = *resultSize + 1;
        result = realloc(result, *resultSize*sizeof(char*));
        result[*resultSize-1] = malloc((n*2+1)*sizeof(char));
        memcpy(result[*resultSize-1],subset,(n*2+1)*sizeof(char));
        //printf("27: %d\n",subset[2*n]=='\0');
        print(result[0]);
        return;
    }

    char components[2] = {'(',')'};

    for(int i = 0; i < sizeof(components)/sizeof(char); i++){
        char component = components[i];
        subset[*subsetSize] = component;
        *subsetSize = *subsetSize + 1;
        if(component == '(') backTrack(n,result,subset,left+1,right,resultSize,subsetSize);
        else if(component == ')') backTrack(n,result,subset,left,right+1,resultSize,subsetSize);
        *subsetSize = *subsetSize - 1;
        //printf("40: %d\n",subset[2*n]=='\0');
    }
}


char ** generateParenthesis(int n, int* returnSize){
    // BackTracking
    // Time Complexity: O(combine(n))
    // Space Complxity: O(combine(n))
    char** result;
    char* subset = malloc((n*2+1)*sizeof(char));
    int* subsetSize = malloc(sizeof(int));
    *subsetSize = 0;
    backTrack(n,result,subset,0,0,returnSize,subsetSize);
    subset[n*2] = '\0';
}

int main(){
    // TODO
    int* returnSize1 = malloc(sizeof(int));
    *returnSize1 = 0;
    char** result1 = generateParenthesis(3,returnSize1);
    printf("ReturnSize is %d\n",*returnSize1);
    printf("Return String is \n");
    // print string
    // for(int i = 0; i < *returnSize1; i++){
    //     printf("{");
    //     print(result1[i]);
    //     printf("}");
    // }
}