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
void deleteduplicates(Node*list,Node*un)
{
    int i=0;
    Node*head=(Node*)malloc(sizeof(Node));
    head=un;
    while(list!=NULL)
    {
        if(i==0)
        {
            i=1;
            un->next=NULL;
            un->val=list->val;
        }
        else
        {
            if(search(head,list->val)==0)
            {
                insertnode(un,list->val);
                un=un->next;
            }
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
    deleteduplicates(l,f);
    display(f);
}