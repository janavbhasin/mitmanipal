#include<stdio.h>
#include<string.h>
#define size 100
typedef struct
{
    char arr[size];
    int f,r;
}queue;
void enqueue(queue*q,char x)
{
    q->r=q->r+1;
    q->arr[q->r]=x;
}
char dequeue(queue*q)
{
    q->f=q->f+1;
    return q->arr[q->f];
}
int main()
{
    char x[100];
    printf("enter the string \n");
    scanf("%s",x);
    int l=strlen(x);
    queue q1,q2;
    q1.f=-1;
    q1.r=-1;
    q2.f=-1;
    q2.r=-1;
    for(int i=0;i<l;i++)
    {
        enqueue(&q1,x[i]);
    }
    for(int i=l-1;i>=0;i--)
    {
        enqueue(&q2,x[i]);
    }
    int flag=0;
    for(int i=0;i<l;i++)
    {
        if(dequeue(&q1)==dequeue(&q2))
        {
            flag=0;
            continue;
        }
        else
        {
            flag=1;
            break;
        }
    }
    if(flag==1)
    {
        printf("its not a palindrome\n");
    }
    else
    {
        printf("its a palindrome\n");
    }
}