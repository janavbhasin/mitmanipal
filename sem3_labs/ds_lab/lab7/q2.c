#include<stdio.h>
#include<stdlib.h>
typedef struct
{
    int*items;
    int hsize,f1,r1,f2,r2;
}queue;
int isFull1(queue q)
{
    if((q.f1==q.r1+1)||(q.f1==0 && q.r1==q.hsize-1))
    {
        return 1;
    }
    else 
    {
        return 0;
    }
}
int isEmpty1(queue q)
{
    if(q.f1==-1)
    {
        return 1;
    }
    else 
    {
        return 0;
    }
}
int isFull2(queue q)
{
    if((q.f2==q.r2+1)||(q.f2==q.hsize && q.r2==(2*q.hsize)-1))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int isEmpty2(queue q)
{
    if(q.f2==q.hsize-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void insert1(queue*q)
{
    if(isFull1(*q)==1)
    {
        printf("queue is full\n");
        return ;
    }
    else
    {
        if(q->f1==-1)
        {
            q->f1=0;
        }
        q->r1=(q->r1+1) % q->hsize;
        printf("enter the element to be queued\n");
        scanf("%d",&(q->items[q->r1]));
    }
}
void insert2(queue*q)
{
    if(isFull2(*q)==1)
    {
        printf("queue is full\n");
    }
    else
    {
        if(q->f2==q->hsize-1)
        {
            q->f2=q->hsize;
        }
        q->r2=((q->r2+1) % q->hsize+q->hsize);
        printf("enter the element to be queued \n");
        scanf("%d",&(q->items[q->r2]));
    }
}
void delete1(queue*q)
{
    if(isEmpty1(*q)==1)
    {
        printf("queue is empty\n");
        return;
    }
    else
    {
        printf("dequeued %d",q->items[q->f1]);
        if(q->f1==q->r1)
        {
            q->f1=-1;
            q->r1=-1;
        }
        else
        {
            q->f1=(q->f1+1) % q->hsize;
        }
    }
}
void delete2(queue*q)
{
    if(isEmpty2(*q)==1)
    {
        printf("queue is empty\n");
        return;
    }
    else
    {
        printf("dequeued %d",q->items[q->f2]);
        if(q->f2==q->r2)
        {
            q->f2=-1;
            q->r2=-1;
        }
        else
        {
            q->f2=((q->f2+1) % (q->hsize*2))+q->hsize;
        }
    }
}
void display(queue q)
{
    if(isEmpty1(q)==1)
    {
        printf("queue1 is empty\n");
        return ;
    }
    else
    {
        int i;
        printf("\n");
        for(i=q.f1;i!=q.r1;i=(i+1) % q.hsize)
        {
            printf("%d->",q.items[i]);
        }
        printf("%d",q.items[i]);
        printf("\n");
    }
    if(isEmpty2(q)==1)
    {
        printf("queue2 is empty\n");
    }
    else
    {
        int i;
        printf("\n");
        for(i=q.f2;i!=q.r2;i=((i+1) % (q.hsize*2))+q.hsize)
        {
            printf("%d->",q.items[i]);
        }
        printf("%d",q.items[i]);
        printf("\n");
    }
}
int main()
{
    int size;
    printf("enter the size of the queue\n");
    scanf("%d",&size);
    queue q;
    q.items=(int*)malloc(size*sizeof(int));
    q.f1=-1;
    q.r1=-1;
    q.hsize=size/2;
    q.f2=q.hsize-1;
    q.r2=q.hsize-1;
    int ch=0;
    while(ch!=6)
    {
        printf("\nenter\n1 for enqueue1\n2 for enqueue2\n3 for dequeue1\n4 for dequeue2\n5 for display\n6 for exit\n");
        scanf("%d",&ch);
        switch (ch)
        {
        case 1:
        insert1(&q);
        break;
        case 2:
        insert2(&q);
        break;
        case 3:
        delete1(&q);
        break;
        case 4:
        delete2(&q);
        break;
        case 5:
        display(q);
        break;
        case 6:
        printf("bye bye\n");
        break;
        }
    }
}