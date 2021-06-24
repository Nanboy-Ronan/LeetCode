#include "HashInteger.h"

typedef struct Entry{
    char *key;
    char *value;
    Entry *next;
} Entry;

typedef struct Table{
    Entry **entries;
}Table;


int hash(int key){
    return key % CAPACITY;
}

Entry* hashEntry(int key, int value){
    Entry* entry = malloc(sizeof(Entry));
    entry->key = malloc(sizeof(int));
    entry->value = malloc(sizeof(int));

    *(entry->key) = key;
    *(entry->value) = value;
    entry->next = NULL;

    return entry;
}

Table* hashTableInit(){
    Table* hashTable = malloc(sizeof(Table));
    hashTable->entries = malloc(CAPACITY*sizeof(Entry*));

    for(int i = 0; i < CAPACITY; i++){
        hashTable->entries[i] = NULL;
    }

    return hashTable;
}

void hashTableDestory(Table* hashtable){
    for(int i = 0; i < CAPACITY; i++){
        if(hashtable->entries[i] != NULL){
            free(hashtable->entries[i]->key);
            free(hashtable->entries[i]->value);
            hashtable->entries[i]->next = NULL;
            free(hashtable->entries[i]);
        }
    }
    free(hashtable->entries);
    free(hashtable);

}

void hashPut(Table* hashtable, int key, int value){
    int slot = hash(key);

    Entry* entry = hashtable->entries[slot];

    if(entry == NULL){
        hashtable->entries[slot] = hashEntry(key, value);
        return;
    }

    Entry* prev;

    while(entry != NULL){
        if(*(entry->key) == key){
            free(entry->value);
            entry->value = malloc(sizeof(int));
            *(entry->value) = value;
            return;
        }

        prev = entry;
        entry = entry->next;
    }

    prev->next = hashEntry(key, value);
}

int hashGet(Table* hashtable, int key){
    int slot = hash(key);

    Entry* entry = hashtable->entries[slot];

    if(entry == NULL) return NULL;

    while(entry != NULL){
        if(*(entry->key) == key) return *(entry->value);

        entry = entry->next;
    }

    return NULL;
}

void hashDelete(Table* hashtable, int key){
    int slot = hash(key);

    Entry* entry = hashtable->entries[slot];

    if(entry == NULL) return;

    Entry* prev;
    int index = 0;

    while(entry != NULL){
        if(*(entry->key) == key){
            if(entry->next == NULL && index == 0) hashtable->entries[slot] = NULL;
            if(entry->next != NULL && index == 0) hashtable->entries[slot] = entry->next;
            if(entry->next == NULL && index != 0) prev->next = NULL;
            if(entry->next != NULL && index != 0) prev->next = entry->next;

            free(entry->key);
            free(entry->value);
            free(entry);
            return;
        }
        prev = entry;
        entry = entry->next;
        index++;
    }
}

void hashPrint(Table *hashtable) {
    for (int i = 0; i < CAPACITY; ++i) {
        Entry *entry = hashtable->entries[i];

        if (entry == NULL) {
            continue;
        }

        printf("slot[%4d]: ", i);

        for(;;) {
            printf("%d=%d ", *(entry->key), *(entry->value));

            if (entry->next == NULL) {
                break;
            }

            entry = entry->next;
        }

        printf("\n");
    }
}

// int main(){
//     Table* table = hashTableInit();
//     hashPut(table, 1, 2);
//     hashPut(table, 3, 4);
//     hashPut(table, 5, 6);
//     hashPut(table, 7, 8);
//     hashPut(table, 9, 10);
//     hashPut(table, 11, 12);
//     hashPut(table, 13, 14);

//     printf("%d\n", hashGet(table, 1));
//     printf("%d\n", hashGet(table, 3));
//     printf("%d\n", hashGet(table, 5));
//     printf("%d\n", hashGet(table, 7));
//     printf("%d\n", hashGet(table, 9));
//     printf("%d\n", hashGet(table, 11));
//     printf("%d\n", hashGet(table, 13));

//     hashPrint(table);
//     hashTableDestory(table);
    
// }