#include<stdio.h>
#include<stdlib.h>
#include"q1.h"
int main()
{
    Node*head=NULL;
    int ch=0;
    while(ch!=6)
    {
        printf("enter\n1 for insertion in start\n2 for insertion at end\n3 for delete at start\n4 for delete at end\n5 for display\n6 for exit\n");
        scanf("%d",&ch);
        if(ch==1)
        {
            int x;
            printf("enter data to be inserted\n");
            scanf("%d",&x);
            head=insertatbeginning(head,x);
        }
        else if(ch==2)
        {
            int x;
            printf("enter data to be inserted\n");
            scanf("%d",&x);
            head=insertatend(head,x);
        }
        else if(ch==3)
        {
            head=deletefirst(head);
        }
        else if(ch==4)
        {
            head=deleteend(head);
        }
        else if(ch==5)
        {
            display(head);
        }
        else if(ch==6)
        {
            printf("bye bye\n");
        }
    }
}