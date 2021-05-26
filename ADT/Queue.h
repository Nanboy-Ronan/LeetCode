/* This defines a queue implemented by a circular array with functions of resizing ip and down */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef char ElementType;

typedef struct Queue Queue;

Queue* QueueInit();

void QueueDestory(Queue* queue);

void enqueue(Queue* queue, ElementType ele);

ElementType dequeue(Queue* queue);

int QueueSize(Queue* queue);

int QueueEmpty(Queue* queue);