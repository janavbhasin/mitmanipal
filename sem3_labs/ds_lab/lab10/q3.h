#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct 
{
    char st[100];
}str;
typedef struct Node
{
    str sti;
    struct Node*next;
    struct Node*prev;
}Node;
Node*createnode(char x[])
{
    Node*newnode=(Node*)malloc(sizeof(Node));
    newnode->next=NULL;
    newnode->prev=NULL;
    strcpy(newnode->sti.st,x);
    return newnode;
}
Node*insert(Node*head,char x[])
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
    while(i!=x)
    {
        i++;
        printf("%s\t",head->sti.st);
        head=head->next;
    }
}
void reverse(Node*head,int x)
{
    int i=0;
    while(i!=x)
    {
        i++;
        head=head->prev;
        printf("%s\t",head->sti.st);
    }
}