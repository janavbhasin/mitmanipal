#include<stdio.h>
#include<stdlib.h>

typedef struct Node 
{
    int val;
    struct Node*next;
    struct Node*prev;
}Node;

Node*creatnode(int x)
{
    Node*newnode=(Node*)malloc(sizeof(Node));
    newnode->next=NULL;
    newnode->prev=NULL;
    newnode->val=x;
    return newnode;
}

Node*insertatbeginning(Node*head,int x)
{
    Node*newnode=creatnode(x);
    if(head==NULL)
    {
        return newnode;
    }
    newnode->next=head;
    head->prev=newnode;
    return newnode;
}

Node*insertatend(Node*head,int x)
{
    Node*newnode=creatnode(x);
    if(head==NULL)
    {
        return newnode;
    }
    Node*temp=head;
    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    temp->next=newnode;
    newnode->prev=temp;
    return head;
}

Node*deletefirst(Node*head)
{
    Node*out=NULL;
    out=head->next;
    return out;
}

Node*deleteend(Node*head)
{
    Node*out=NULL;
    while(head->next!=NULL)
    {
        out=insertatend(out,head->val);
        head=head->next;
    }
    return out;
}

void display(Node*head)
{
    while(head!=NULL)
    {
        printf("%d->",head->val);
        head=head->next;
    }
    printf("NULL\n");
}