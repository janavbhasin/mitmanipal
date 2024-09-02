#include<stdio.h>
#include<stdlib.h>
#include"q3.h"
int main()
{
    Node*head=NULL;
    int i=0,ch=0;
    while(ch!=4)
    {
        printf("\nenter\n1 for enter\n2 for display\n3 for reverse\n4 for exit\n");
        scanf("%d",&ch);
        if(ch==1)
        {
            char x[10];
            printf("enter string\n");
            scanf("%s",x);
            head=insert(head,x);
            i++;
        }
        else if(ch==2)
        {
            display(head,i);
        }
        else if(ch==3)
        {
            reverse(head,i);
        }
        else if(ch==4)
        {
            printf("bye bye\n");
        }
    }
}