#include<stdio.h>
#include<stdlib.h>
#include"functions.h"
void insertafter(Node*list,int x,Node*new,int y)
{
    while(list!=NULL)
    {
        insertnode(new,list->val);
        new=new->next;
        if(list->val==x)
        {
            insertnode(new,y);
            new=new->next;
        }
        list=list->next;
    }
}
int main()
{
    int n;
    printf("enter number of elements in list: ");
    scanf("%d", &n);
    Node *l = (Node *)malloc(sizeof(Node));
    Node *f = (Node *)malloc(sizeof(Node));
    printf("enter elements of list:\n");
    input(l, n);
    display(l);
    int a,b;
    printf("enter number after");
    scanf("%d",&a);
    printf("enter number to be inserted");
    scanf("%d",&b);
    insertafter(l,a,f,b);
    display(f->next);
}