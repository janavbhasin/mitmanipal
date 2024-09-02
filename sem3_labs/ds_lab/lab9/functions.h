#include<stdio.h>
#include<stdlib.h>
typedef struct node
{
    int val;
    struct node*next;
}node;

typedef struct node Node;
void insertnode(Node*,int);
void display(Node*);
void deltenode(Node**,Node*);
void input(Node*,int);

void insertnode(Node*prev,int x)
{
    Node*t=(Node*)malloc(sizeof(Node));
    t->next=prev->next;
    t->val=x;
    prev->next=t;
}
void deletenode(Node**list,Node*tbd)
{
    if(*list==tbd)
    {
        (*list)=(*list)->next;
    }
    else
    {
        Node*temp=(Node*)malloc(sizeof(Node));
        while(temp->next!=NULL)
        {
            if(temp->next==tbd)
            {
                temp->next=tbd->next;
                break;
            }
            temp=temp->next;
        }
    }
    free(tbd);
}
void display(Node*node)
{
    while(node!=NULL)
    {
        printf("%d\t",node->val);
        node=node->next;
    }
    printf("\n");
}
void input(Node*node,int n)
{
    int i,temp;
    for(i=0;i<n;i++)
    {
        printf("enter the value\n");
        scanf("%d",&temp);
        if(i==0)
        {
            node->next=NULL;
            node->val=temp;
            continue;
        }
        insertnode(node,temp);
        node=node->next;
    }
}