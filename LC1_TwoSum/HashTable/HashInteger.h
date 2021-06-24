#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* This defines a simple hash table (integer, integer) with seperate chain */
#define CAPACITY 100000

typedef struct Entry Entry;

typedef struct Table Table;

int hash(int key);

Entry* hashEntry(int key, int value);

Table* hashTableInit();

void hashTableDestory(Table* hashtable);

void hashPut(Table* hashtable, int key, int value);

int hashGet(Table* hashtable, int key);

void hashDelete(Table* hashtable, int key);