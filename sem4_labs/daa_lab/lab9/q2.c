#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define HASH_TABLE_SIZE 10
struct node 
{
    char *data;
    struct node *next;
};
int hash(char *str)
{
    int hash = 0;
    while (*str)
    {
        hash =hash+(*str++)-97;
    }
    return hash % HASH_TABLE_SIZE;
}
struct node *chain[HASH_TABLE_SIZE];
int comparisons = 0; 
void init()
{
    int i;
    for(i = 0; i < HASH_TABLE_SIZE; i++)
    {
        chain[i] = NULL;
    }
}
void insert(char *value) 
{
    struct node *newNode = malloc(sizeof(struct node));
    newNode->data = value;
    newNode->next = NULL;
    int key = hash(value);
    if(chain[key] == NULL)
    {
        chain[key] = newNode;
    }
    else 
    {
        struct node *temp = chain[key];
        while(temp->next!=NULL)
        {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}
int search(char *key) 
{
    int index = hash(key);
    struct node *temp = chain[index];
    comparisons = 0;
    while(temp != NULL) 
    {
        comparisons++;
        if(strcmp(temp->data, key) == 0)
        {
            return 1;
        }
        temp = temp->next;
    }
    return 0;
}
void print() 
{
    int i;  
    for(i = 0; i < HASH_TABLE_SIZE; i++) 
    {
        struct node *temp = chain[i];
        printf("chain[%d]->", i);
        while(temp) 
        {
            printf("%s ->", temp->data);
            temp = temp->next;
        }
        printf("NULL\n");
    }
}
int main() 
{
    init();
    insert("apple");
    insert("banana");
    insert("cherry");
    insert("dog");
    insert("elephant");
    insert("frog");
    insert("ok");
    insert("not");
    insert("daa");
    insert("tell");
    insert("me");
    insert("why");
    insert("aint");
    insert("nothing");    
    insert("but");
    insert("a");
    insert("heart");
    insert("break");
    print();
    char *key_to_search = "elephant";
    if(search(key_to_search))
    {
        printf("Key %s found with %d comparisons\n", key_to_search, comparisons);
    }
    else
    {
        printf("Key %s not found with %d comparisons\n", key_to_search, comparisons);
    }
    key_to_search = "zebra";
    if(search(key_to_search))
    {
        printf("Key %s found with %d comparisons\n", key_to_search, comparisons);
    }
    else
    {
        printf("Key %s not found with %d comparisons\n", key_to_search, comparisons);
    }
}