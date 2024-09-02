#include<stdio.h>
#define size 100
typedef struct
{
    int arr[size];
    int f,r;
}queue;
int isFull(queue q)
{
    if(q.f==q.r+1)
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
void sort(queue*q)
{
    int index;
    for(int i=0;i!=(q->r+1)%size;i=(i+1)%size)
    {
        index=i;
        for(int j=i+1;j!=(q->r+1)%size;j=(j+1)%size)
        {
            if(q->arr[index]>q->arr[j])
            {
                index=j;
            }
        }
        int x=q->arr[index];
        q->arr[index]=q->arr[i];
        q->arr[i]=x;
    }
}
void pqinsert(queue*q,int x)
{
    if(isFull(*q)==1)
    {
        printf("queue is empty\n");
        return;
    }
    else
    {
        if(q->f==-1)
        {
            q->f=0;
        }
        q->r=(q->r+1)%size;
        q->arr[q->r]=x;
        sort(q);
    }
}

void pqdelete(queue*q)
{
    if(isEmpty(*q)==1)
    {
        printf("queue is empty\n");
        return;
    }
    else
    {
        if(q->f==q->r)
        {
            q->f=-1;
            q->r=-1;
        }
        sort(q);
        printf("%d dequeued\n",q->arr[q->f]);
        q->f=(q->f+1)%size;
    }
}
void display(queue q)
{
    if(isEmpty(q))
    {
        printf("queue is empty\n");
        return;
    }
    else
    {
        sort(&q);
        int i;
        for(i=q.f;i!=q.r;i=(i+1)%size)
        {
            printf("%d\t",q.arr[i]);
        }
        printf("%d\t",q.arr[i]);
    }
}
int main()
{
    queue q;
    q.f=-1;
    q.r=-1;
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
            pqinsert(&q,x);
        }
        else if(ch==2)
        {
            pqdelete(&q);
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