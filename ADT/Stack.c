#include "Stack.h"
/* This is a stack implemented by array with functions of resize ip and down */
typedef struct Stack{
    ElementType* a; // array
    int top;
    int capacity;
}Stack;

Stack* StackInit(){
    Stack* stack = malloc(sizeof(Stack));
    stack->a = malloc(sizeof(ElementType)*10);
    stack->top = 0;
    stack->capacity = 10;
    return stack;
}

void StackDestory(Stack* stack){
    free(stack->a);
    free(stack);
}

void StackPush(Stack* stack, ElementType ele){
    assert(stack);
    /* if full then resize my multiply a constant */
    if(stack->top == stack->capacity){
        stack->a = realloc(stack->a, 2*stack->capacity*sizeof(ElementType));
        stack->capacity *= 2;
    }
    stack->a[stack->top] = ele;
    stack->top++;
}

ElementType StackPop(Stack* stack){
    assert(stack);
    /* Resize if the size of the array is one quarter of its capacity */
    if(stack->top < 0.25*stack->capacity){
        ElementType* a = malloc(0.25*stack->capacity*sizeof(ElementType));
        for(int i = 0; i <= stack->top - 1; i++){
            a[i]=stack->a[i];
        }
        free(stack->a);
        stack->a = a;
        stack->capacity = 0.25*stack->capacity;
    }
    ElementType temp;
    if(stack->top > 0){
        temp = stack->a[stack->top - 1];
        stack->top --;
    }
    return temp;
}

ElementType StackPeek(Stack* stack){
    assert(stack);
    return stack->a[stack->top - 1];
}

int StackSize(Stack* stack){
    assert(stack);
    return stack->top;
}

int StackEmpty(Stack* stack){
    assert(stack);
    return stack->top == 0? 1 : 0;
}
