#include<stdio.h>
#include<stdlib.h>
#define size 100
typedef struct
{
    int arr[size];
    int top;
}stack;
int isempty(stack*st)
{
    if(st->top==-1)
    {
        return 1;
    }
    else 
    {
        return 0;
    }
}
int isfull(stack*st)
{
    if (st->top==size-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void push(stack*st,int item)
{
    st->top++;
    st->arr[st->top]=item;
}
void pop(stack*st)
{
    printf("%d popped\n",st->arr[st->top]);
    st->top--;
}
int main()
{
    int i=0;
    stack*st=(stack*)calloc(1,sizeof(stack));
    while(i!=3)
    {
        printf("1=push\n2=po\n3=exit");
        scanf("%d",&i);
        if(i==1)
        {
            int item;
            scanf("%d",&item);
            push(st,item);
        }
        else if(i==2)
        {
            pop(st);
        }
        else if(i==3)
        {
            printf("bye bye\n");
        }
    }
}