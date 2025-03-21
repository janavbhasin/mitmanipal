#include<stdio.h>
#include<stdlib.h>
#include"functions.h"
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
void getunion(Node*l1,Node*l2,Node*un)
{
    int i=0;
    Node*unhead=(Node*)malloc(sizeof(Node));
    unhead=un;
    while(l1!=NULL)
    {
        if(i==0)
        {
            i=1;
            un->next=NULL;
            un->val=l1->val;
        }
        else
        {
            if(search(l2,l1->val)==0)
            {
                insertnode(un,l1->val);
                un=un->next;
            }
        }
        l1=l1->next;
    }
    while(l2!=NULL)
    {
        if(search(unhead,l2->val)==0)
        {
            insertnode(un,l2->val);
            un=un->next;
        }
        l2=l2->next;
    }
}
void intersection(Node*l1,Node*l2,Node*inter)
{
    int i=0;
    while(l1!=NULL)
    {
        if(search(l2,l1->val)==1)
        {
            if(i==0)
            {
                i=1;
                inter->next=NULL;
                inter->val=l1->val;
            }
            else
            {
                insertnode(inter,l1->val);
                inter=inter->next;
            }
        }
        l1=l1->next;
    }
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

    printf("enter elements of list 1:\n");
    input(l1, n1);
    printf("enter elements of list 2:\n");
    input(l2, n2);
    printf("list 1: ");
    display(l1);
    printf("list 2: ");
    display(l2);
    printf("union: ");
    getunion(l1, l2, unionl);
    display(unionl);
    printf("intersection: ");
    if (n1 <= n2)
        intersection(l1, l2, inter);
    else
        intersection(l2, l1, inter);
    display(inter);
}