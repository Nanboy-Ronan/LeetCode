/* Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
* An input string is valid if:
* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.

* Input: s = "()[]{}"
* Output: true
* Input: s = "(]"
* Output: false
* Input: s = "([)]"
* Output: false
* Input: s = "{[]}"
* Output: true
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "Stack.h"


bool isValid(char *str){
    Stack* stack = StackInit();

    while(*str){
        if(*str == '(' || *str == '[' || *str == '{'){
            StackPush(stack, *str);
        }else{
            if(StackEmpty(stack)) return false;
            char temp = StackPop(stack);
            if(temp == '(' && *str != ')') return false;
            if(temp == '[' && *str != ']') return false;
            if(temp == '{' && *str != '}') return false;
        }
        str++;
    }
    bool retVal = StackEmpty(stack)? true : false;
    StackDestory(stack);
    return retVal;
}

int main(){
    printf("%d\n", isValid(""));
    printf("%d\n", isValid("()[]{}"));
    printf("%d\n", isValid("(]"));
    printf("%d\n", isValid("([)]"));
    printf("%d\n", isValid("{[]}"));
    printf("%d\n", isValid("()[]{}("));
    printf("%d\n", isValid("()[]{})"));
}