#include<stdio.h>
#include<stdlib.h>
#include"q2.h"
Node*add(Node*head1,int x,Node*head2,int y)
{
    Node*out=NULL;
    int i=0,j=0;
    while((i!=x)&&(j!=y))
    {
        out=insert(out,(head1->val)+(head2->val));
        head1=head1->next;
        head2=head2->next;
        i++;
        j++;
    }
    if(i!=x)
    {
        while(i!=x)
        {
            out=insert(out,head1->val);
            head1=head1->next;
            i++;
        }
    }
    else if(j!=y)
    {
        while(j!=y)
        {
            out=insert(out,head2->val);
            head2=head2->next;
            j++;
        }
    }
    return out;
}
int main()
{
    Node*head1=NULL;
    Node*head2=NULL;
    long int n1,n2;
    printf("enter the number\n");
    scanf("%ld",&n1);
    printf("enter the number\n");
    scanf("%ld",&n2);
    long int copy1=n1,copy2=n2;
    int l1=0,l2=0;
    while(n1!=0)
    {
        n1=n1/10;
        l1++;
    }
    while(n2!=0)
    {
        n2=n2/10;
        l2++;
    }
    printf("l1:%d\n",l1);
    printf("l2:%d\n",l2);
    if(l1>l2)
    {
        while(copy1!=0)
        {
            head1=insert(head1,copy1%10);
            copy1=copy1/10;
        }
        while(copy2!=0)
        {
            head2=insert(head2,copy2%10);
            copy2=copy2/10;
        }
        Node*head=NULL;
        head=add(head1,l1,head2,l2);
        display(head,l1);
    }
}