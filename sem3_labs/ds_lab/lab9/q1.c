#include<stdio.h>
#include<stdlib.h>
#include"functions.h"
int isEmpty(Node*list)
{
    if(list==NULL)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void enqueue(Node**list,int x)
{
    Node*new=(Node*)malloc(sizeof(Node));
    if(isEmpty(*list)==1)
    {
        *list=new;
        (*list)->val=x;
        (*list)->next=NULL;
    }
    else
    {
        new=*list;
        while(new->next!=NULL)
        {
            new=new->next;
        }
        insertnode(new,x);
    }
}

int dequeue(Node**list)
{
    int i=0;
    if(isEmpty(*list)==1)
    {
        printf("queue is empty\n");
        return -5;
    }
    else
    {
        int x=(*list)->val;
        deletenode(list,*list);
        return x;
    }
}
int main()
{
    int x,inp=0,i=0;
    Node*list=(Node*)malloc(sizeof(Node));
    list=NULL;
    while(inp!=3)
    {
        printf("\nenter\n1 for enqueue\n2 for dequeue\n3 for exit\n");
        scanf("%d",&inp);
        if(inp==1)
        {
            printf("enter the value\n");
            scanf("%d",&x);
            enqueue(&list,x);
        }
        else if(inp==2)
        {
            printf("dequeued %d\n",dequeue(&list));
        }
        else if(inp==3)
        {
            printf("bye bye\n");
        }
    }
}