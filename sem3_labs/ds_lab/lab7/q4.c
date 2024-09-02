#include<stdio.h>
#include<stdlib.h>
#define SIZE 100
typedef struct
{
    int arr[SIZE];
    int top;
}Stack;
int isFull(Stack st)
{
    if(st.top==SIZE-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int isEmpty(Stack st)
{
    if(st.top==-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void push(Stack*st,int x)
{
    if(isFull(*st)==1)
    {
        printf("stack is full\n");
        return;
    }
    else
    {
        st->top=(st->top)+1;
        st->arr[st->top]=x;
    }
}
int pop(Stack*st)
{
    if(isEmpty(*st)==1)
    {
        printf("stack is empty\n");
        exit(1) ;
    }
    else
    {
        int x;
        x=st->arr[st->top];
        st->top=st->top-1;
        return x;
    }
}
void enqueue(Stack*st1,Stack*st2,int value)
{
    while(isEmpty(*st1)!=1)
    {
        push(st2,pop(st1));
    }
    push(st1,value);
    while (isEmpty(*st2)!=1)
    {
        push(st1,pop(st2));
    }
}
void dequeue(Stack*st)
{
    if(isEmpty(*st)==1)
    {
        printf("queue is enmpty");
        
    }
    else
    {
        printf("popped element %d",pop(st));
    }
}
void display(Stack st)
{
    if(isEmpty(st)==1)
    {
        printf("queue is empty\n");
    }
    else
    {
        printf("queue is :\n");
        for(int i=st.top;i>=0;i--)
        {
            printf("%d\t",st.arr[i]);
        }
    }
}
int main()
{
    Stack st1,st2;
    st1.top=-1;
    st2.top=-1;
    int ch=0;
    while(ch!=4)
    {
        printf("\nenter\n1 for enqueue\n2 for dequeue\n3 for display\n4 for exit\n");
        scanf("%d",&ch);
        if(ch==1)
        {
            int x;
            printf("enter the element to be queued\n");
            scanf("%d",&x);
            enqueue(&st1,&st2,x);
        }
        else if(ch==2)
        {
            dequeue(&st1);
        }
        else if(ch==3)
        {
            display(st1);
        }
        else if(ch==4)
        {
            printf("bye bye\n");
        }
    }
}