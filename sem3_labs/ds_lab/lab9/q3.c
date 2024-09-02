#include<stdio.h>
#include<stdlib.h>
#include"functions.h"
void merge(Node*l1,Node*l2,Node*un)
{
    while(l1!=NULL)
    {
        insertnode(un,l1->val);
        l1=l1->next;
        un=un->next;
    }
    while(l2!=NULL)
    {
        insertnode(un,l2->val);
        l2=l2->next;
        un=un->next;
    }
}
void sort(Node*list)
{
    Node*copy=list;
    while(list!=NULL)
    {
        copy=list->next;
        while(copy!=NULL)
        {
            if((list->val)>(copy->val))
            {
                int temp=list->val;
                list->val=copy->val;
                copy->val=temp;
            }
            copy=copy->next;
        }
        list=list->next;
    }
}
int main()
{
    int n1, n2, x;
    printf("enter number of students in class a: ");
    scanf("%d", &n1);
    printf("enter number of students in class b: ");
    scanf("%d", &n2);
    Node *l1 = (Node *)malloc(sizeof(Node));
    Node *l2 = (Node *)malloc(sizeof(Node));
    Node *sorted = (Node *)malloc(sizeof(Node));
    printf("enter students of class a:\n");
    input(l1, n1);
    printf("enter students of class b:\n");
    input(l2, n2);
    printf("class a: ");
    display(l1);
    printf("class b: ");
    display(l2);
    merge(l1,l2,sorted);
    sort(sorted);
    display(sorted->next);
}