#include<stdio.h>
#include<stdlib.h>

typedef struct Node
{
    int val;
    struct Node*next;
}Node;

void insertnode(Node*prev,int x)
{
    Node*newnode=(Node*)malloc(sizeof(Node));
    newnode->next=prev->next;
    prev->next=newnode;
    newnode->val=x;
}

Node*newnode(Node*prev,int x)
{
    Node*newnode=(Node*)malloc(sizeof(Node));
    newnode->next=prev->next;
    prev->next=newnode;
    newnode->val=x;
    return newnode;
}

int search(Node*list,int x)
{
    while(list!=NULL)
    {
        if(list->val==x)
        {
            return 1;
        }
        list=list->next;
    }
    return 0;
}

void getunion(Node*a,Node*b,Node*un)
{
    int i=0;
    Node*unhead=(Node*)malloc(sizeof(Node));
    unhead=un;
    while(a!=NULL)
    {
        if(i==0)
        {
            i=1;
            un->next=NULL;
            un->val=a->val;
        }
        else
        {
            if(search(b,a->val)==0)
            {
                insertnode(un,a->val);
                un=un->next;
            }
        }
        a=a->next;
    }
    while(b!=NULL)
    {
        if(search(un,b->val)==0)
        {
            insertnode(un,b->val);
            un=un->next;
        }
        b=b->next;
    }
}

void enqueue(Node**list,int x)
{
    Node*new=(Node*)malloc(sizeof(Node));
    if(*list==NULL)
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

void intersection(Node*a,Node*b,Node*inter)
{
    int i=0;
    Node*unhead=(Node*)malloc(sizeof(Node));
    unhead=inter;
    while (a!=NULL)
    {
        if(search(b,a->val)==1)
        {
            if(i==0)
            {
                i=1;
                inter->next=NULL;
                inter->val=a->val;
            }
            else
            {
                insertnode(inter,a->val);
                inter=inter->next;
            }
        }
        a=a->next;
    }
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

int main()
{
    int n1, n2, x;
    printf("enter number of elements in list 1: ");
    scanf("%d", &n1);
    printf("enter number of elements in list 2: ");
    scanf("%d", &n2);
    Node *l1 = (Node *)malloc(sizeof(Node));
    Node *l2 = (Node *)malloc(sizeof(Node));
    Node *inter = (Node *)malloc(sizeof(Node));
    Node *unionl = (Node *)malloc(sizeof(Node));
    int i=0,j=0;
    while(i!=n1)
    {
        printf("enter elements of list 1:\n");
        scanf("%d",&x);
        enqueue(&l1,x);
        i=i+1;
    }
    while(j!=n2)
    {
        printf("enter elements of list 2:\n");
        scanf("%d",&x);
        enqueue(&l2,x);
        j=j+1;
    }
    printf("list 1: ");
    display(l1);
    printf("list 2: ");
    display(l2);
    printf("union: ");
    getunion(l1, l2, unionl);
    display(unionl);
    printf("intersection: ");
    if (n1 <= n2)
    {
        intersection(l1, l2, inter);
    }
    else
    {
        intersection(l2, l1, inter);
    }
    display(inter);
}