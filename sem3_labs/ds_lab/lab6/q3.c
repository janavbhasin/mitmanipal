#include<stdio.h>
#define SIZE 10
int top1=-1;
int top2=SIZE;
int arr[SIZE];
void push1(int x)
{
    if(top1<top2-1)
    {
        arr[++top1] = x;
        printf("%d pushed in stack 1\n", x);
    }
    else
    {
        printf("stack full\n");
    }
}
void push2(int x)
{
    if(top1<top2-1)
    {
        arr[--top1] = x;
        printf("%d pushed in stack 2\n", x);
    }
    else
    {
        printf("stack full\n");
    }
}
void pop1()
{
    if(top1>=0)
    {
        int x=arr[(top1)--];
        printf("popped %d\n",x);
    }
}
void pop2()
{
    if(top1>=0)
    {
        int x=arr[(top2)++];
        printf("popped %d\n",x);
    }
}
void print1()
{
    for (int i=top1;i>=0;i--)
    {
        printf("%d",arr[i]);
    }
}
void print2()
{
    for(int i=top2;i<=SIZE;i++)
    {
        printf("%d",arr[i]);
    }
}
int main()
{
    int a[SIZE];
    int i, n;
    for (i = 0; i <= 2; i++)
    {
        push1(i);
    }
    for (i = 1; i <= 3; i++)
    {
        push2(i);
    }
    print1();
    print2();
    push1(11);

    n = top1 + 1;
    while (n)
    {
        pop1();
        n--;
    }
    pop1();
}