#include<stdio.h>
#include<stdlib.h>
#define max 10
typedef struct stack
{
    int tos;
    int arr[max];
}STACK;
int isempty(STACK s)
{
    if (s.tos==-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int isfull(STACK s)
{
    if(s.tos==max)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void push(STACK*s,int n)
{
    if (isfull(*s)==1)
    {
        printf("stack overflow");
        return;
    }
    else
    {
        s->tos=s->tos+1;
        s->arr[s->tos]=n;
        return;
    }
}
int pop(STACK*s)
{
    if(isempty(*s)==1)
    {
        printf("the stack is empty");
        return 1;
    }
    else
    {
        s->tos=s->tos-1;
        return s->arr[s->tos];
    }
}
void peak(STACK*s)
{
    s->tos=s->tos-1;
    printf("%d",s->arr[s->tos]);
    s->tos=s->tos+1;
}
void display(STACK s)
{
    for(int i=0;i<=s.tos;i++)
    {
        printf("%d\n",s.arr[i]);
    }
}
int main()
{
    int input=0;
    STACK *s = (STACK *)malloc(sizeof(STACK));
    s->tos = -1;
    while(input!=3)
    {
        printf("Do you want to push, pop or exit? (1/2/3) ");
        scanf("%d", &input);
        int out;
        switch (input)
        {
        case 1:
            printf("Enter the character to push: ");
            int in;
            scanf("%d", &in);
            push(s, in);
            display(*s);
            break;
        case 2:
            out = pop(s);
            printf("Popped %d \n", out);
            display(*s);
            break;

        case 3:
            printf("Bye Bye\n");
            break;
        default:
            break;
        }
    }
    free(s);
}