#include<stdio.h>
typedef struct 
{
    char str[10];
}st;
typedef struct 
{
    st arr[100];
    int f,r;
}queue;
int isFull(queue q)
{
    if ((q.f==q.r+1)||(q.f==0&&q.r==99))
    {
        return 1;
    }
    else 
    {
        return 0;
    }
}
int isEmpty(queue q)
{
    if(q.f==-1)
    {
        return 1;
    }
    else 
    {
        return 0;
    }
}
void enqueue(queue*q)
{
    if(isFull(*q)==1)
    {
        printf("queue is full\n");
        return;
    }
    else
    {
        if(q->f==-1)
        {
            q->f=0;
        }
        char x[10];
        printf("enter the element to be queued\n");
        scanf("%s",q->arr[q->r].str);
        printf("queued %s\n",q->arr[q->r].str);
        q->r=(q->r+1)%100;
    }
}
void dequeue(queue*q)
{
    if(isEmpty(*q)==1)
    {
        printf("queue is empty\n");
        return;
    }
    else
    {
        printf("dequed %s\n",q->arr->str[q->f]);
        if(q->f==q->r)
        {
            q->f=-1;
            q->r=-1;
        }
        else
        {
            q->f=(q->f+1)%100;
        }
    }
}
void display(queue q)
{
    if(isEmpty(q)==1)
    {
        printf("queue is empty\n");
        return ;
    }
    int i;
    printf("queue is\n");
    for(i=q.f;i!=q.r;i=(i+1)%100)
    {
        printf("%s->",q.arr->str[i]);
    }
    printf("%s",q.arr->str[i]);
}
int main()
{
    int ch=0;
    queue q;
    q.f=q.r=-1;
    while(ch!=4)
    {
        printf("enter\n1 for enqueue\n2 for dequeue\n3 for display\n4 for exit\n");
        scanf("%d",&ch);
        if(ch==1)
        {
            enqueue(&q);
        }
        else if(ch==2)
        {
            dequeue(&q);
        }
        else if(ch==3)
        {
            display(q);
        }
        else if(ch==4)
        {
            printf("bye bye\n");
        }
    }
}