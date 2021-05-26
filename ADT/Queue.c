#include "Queue.h"

/* This is a queue implemented by a circular array with functions of resizing ip and down */
typedef struct Queue{
    ElementType* a; // array
    int front;
    int rear;
    int numOfElements;
    int capacity;
}Queue;

Queue* QueueInit(){
    Queue* queue = malloc(sizeof(Queue));
    queue->a = malloc(sizeof(ElementType)*10);
    queue->front = -1;
    queue->rear = -1;
    queue->numOfElements = 0;
    queue->capacity = 10;
}

void QueueDestory(Queue* queue){
    free(queue->a);
    free(queue);
}

void enqueue(Queue* queue, ElementType ele){
    assert(queue);
    /* if full then resize my multiply a constant */
    if(queue->numOfElements == queue->capacity){
        queue->a = realloc(queue->a, 2*queue->capacity*sizeof(ElementType));
        queue->front = 0;
        queue->rear = queue->numOfElements -1;
        queue->capacity *= 2;
    }
    if(queue->front == -1 && queue->rear == -1){
        queue->front = 0;
        queue->rear = 0;
    }else{
        queue->rear = (queue->rear + 1) % queue->capacity;
    }
    queue->a[queue->rear] = ele;
    queue->numOfElements++;
}

ElementType dequeue(Queue* queue){
    assert(queue);
    /* Resize if the size of the array is one quarter of its capacity */
    if(queue->numOfElements < 0.25*queue->capacity){
        ElementType* a = malloc(0.25*queue->capacity*sizeof(ElementType));
        int index = 0;
        for(int i = queue->front; i <= queue->rear; i++){
            a[index]=queue->a[i];
            index++;
        }
        free(queue->a);
        queue->a = a;
        queue->front = 0;
        queue->rear = queue->numOfElements - 1;
        queue->capacity = 0.25*queue->capacity;

    }
    ElementType temp;
    if(queue->numOfElements > 0){
        temp = queue->a[queue->front];
        if(queue->front == queue->rear){
            queue->front = -1;
            queue->rear = -1;
        }else{
            queue->front = (queue->front + 1) % queue->capacity;
            queue->numOfElements--;
        }
    }
    return temp;
}

int QueueSize(Queue* queue){
    assert(queue);
    return queue->numOfElements;
}

int QueueEmpty(Queue* queue){
    assert(queue);
    return queue->numOfElements == 0? 1 : 0;
}