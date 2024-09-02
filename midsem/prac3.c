#include<stdio.h>
#include<stdlib.h>
#define size 100
typedef struct abc
{
    int arr[size];
    int front ,rear;
}Queue;
int isfull(Queue*queue)
{
    if((queue->rear+1)%size==queue->front)
    {
        printf("queue is full\n");
        return 1;
    }
    else 
    {
        return 0;
    }
}
int isempty(Queue*queue)
{
    if(queue->front==-1&&queue->rear==-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void enque(Queue*queue,int item)
{
    if (isfull(queue)==1)
    {
        return ;
    }
    else if(isempty(queue)==1)
    {
        queue->front=queue->rear=0;
    }
    else
    {
        queue->rear=(queue->rear+1)%size;
    }
    queue->arr[queue->rear]=item; 
}
int deque(Queue*queue)
{
    int item;
    if(isempty(queue)==1)
    {
        printf("the queue is empyt cant print anything\n");
        return 0;
    }
    else
    {
        item=queue->arr[queue->front];
        if(queue->rear==queue->front)
        {
            queue->front=queue->rear=0;
        }
        else
        {
            queue->front=(queue->front+1)%size;
        }
    }
    return item;
}
void display(Queue*queue)
{
    if (isempty(queue))
    {
        printf("the queue is empty, nothing to display\n");
        return;
    }
    for(int i=queue->front;i<=queue->rear;i++)
    {
        printf("%d\n",queue->arr[i]);
    }
}
int main()
{
    Queue*queue=(Queue*)calloc(1,sizeof(Queue));
    queue->front=-1;
    queue->rear=-1;
    int i=0;
    while(i!=4)
    {
        printf("enter 1 for enque\nenter 2 for deque\nenter 3 for display\nenter 4 for exit\n");
        scanf("%d",&i);
        if(i==1)
        {
            int item;
            printf("enter the number to be queued\n");
            scanf("%d",&item);
            enque(queue,item);
        }
        else if(i==2)
        {
            printf("dequed %d\n",deque(queue));
        }
        else if(i==3)
        {
            printf("the current queue is\n");
            display(queue);
        }
        else if(i==4)
        {
            printf("bye bye\n");
        }
    }
}