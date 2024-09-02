#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define size 100
typedef struct
{
    char st[10];
}st;
typedef struct 
{
    st str[size];
    int f,r;
}queue;
void enqueuef(queue*q)
{
    char x[10];
    printf("enter the string\n");
    scanf("%s",x);
    if(q->f==-1)
    {
        q->f=0;
        q->r=0;
        strcpy(q->str[q->f].st,x);
    }
    else
    {
        q->f=(q->f-1+size)%size;
        strcpy(q->str[q->f].st,x);
    }
}
void enqueuer(queue*q)
{
    char x[10];
    printf("enter the string to be queued\n");
    scanf("%s",x);
    if(q->f==-1)
    {
        q->f=0;
    }
    q->r=(q->r+1)%size;
    strcpy(q->str[q->r].st,x);
}
void dequeuef(queue*q)
{
    if((q->f==q->r)&&(q->r==size-1))
    {
        printf("queue is empty\n");
        return ;
    }
    else
    {
        printf("%s",q->str[q->f].st);
        q->f=(q->f+1)%size;
        return ;
    }
}
void display(queue q)
{
    for(int i=q.f;i!=q.r;i=(i+1)%size)
    {
        printf("%s\t",q.str[i].st);
    }
    printf("%s\t",q.str[q.r].st);
}
int main()
{
    queue q;
    q.f=-1;
    q.r=-1;
    int ch=0;
    while(ch!=5)
    {
        printf("\nenter\n1 for enqueuef\n2 for enqueuer\n3 for dequeuef\n4 for display\n5 for exit\n");
        scanf("%d",&ch);
        if(ch==1)
        {
            enqueuef(&q);
        }
        else if(ch==2)
        {
            enqueuer(&q);
        }
        else if(ch==3)
        {
            dequeuef(&q);
        }
        else if (ch==4)
        {
            display(q);
        }
        else if(ch==5)
        {
            printf("bye bye\n");
        }
    }
}