#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#define size 10
struct node
{
    char*string;
    struct node*next;
};
struct node*chain[size];
int hash(char*value)
{
    int hash=0;
    while(*value)
    {
        hash=hash+(*value++)-97;
    }
    return hash%size;
}
void init()
{
    for(int i=0;i<size;i++)
    {
        chain[i]=NULL;
    }
}
void insert(char*value)
{
    struct node*newnode=malloc(sizeof(struct node));
    newnode->string=value;
    newnode->next=NULL;
    int key =hash(value);
    if(chain[key]==NULL)
    {
        chain[key]=newnode;
    }
    else 
    {
        struct node*temp=chain[key];
        while(temp->next!=NULL)
        {
            temp=temp->next;
        }
        temp->next=newnode;
    }
}
int search(char*value)
{
    struct node*temp;
    int index=hash(value);
    temp=chain[index];
    while(temp!=NULL)
    {
        if(strcmp(temp->string,value)==0)
        {
            return 1;
        }
        temp=temp->next;
    }
    return 0;
}
void print() 
{
    int i;  
    for(i = 0; i < size; i++) 
    {
        struct node *temp = chain[i];
        printf("chain[%d]->", i);
        while(temp) 
        {
            printf("%s ->", temp->string);
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
        printf("Key %s found \n", key_to_search);
    }
    else
    {
        printf("Key %s not found \n", key_to_search);
    }
    key_to_search = "zebra";
    if(search(key_to_search))
    {
        printf("Key %s found \n", key_to_search);
    }
    else
    {
        printf("Key %s not found \n", key_to_search);
    }
}