#include<stdio.h>
#include<stdlib.h>

typedef struct Node
{
    int val;
    struct Node*next;
    struct Node*prev;
}Node;

Node*createnode(int x)
{
    Node*newnode=(Node*)malloc(sizeof(Node));
    newnode->next=NULL;
    newnode->prev=NULL;
    newnode->val=x;
    return newnode;
}

Node*insert(Node*head,int x)
{
    Node*newnode=createnode(x);
    if(head==NULL)
    {
        newnode->next=newnode;
        newnode->prev=newnode;  
        return newnode;
    }
    newnode->next=head;
    newnode->prev=head->prev;
    (head->prev)->next=newnode;
    head->prev=newnode;
    return head;
}

void display(Node*head,int x)
{
    int i=0;
    head=head->prev;
    while(i!=x)
    {
        printf("%d\t",head->val);
        i++;
        head=head->prev;
    }
}