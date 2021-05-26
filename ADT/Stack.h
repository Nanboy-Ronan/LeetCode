/* This defines a stack implemented by array with functions of resize ip and down */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef char ElementType;

typedef struct Stack Stack;

Stack* StackInit();

void StackDestory(Stack* stack);

void StackPush(Stack* stack, ElementType ele);

ElementType StackPop(Stack* stack);

ElementType StackPeek(Stack* stack);

int StackSize(Stack* stack);

int StackEmpty(Stack* stack);