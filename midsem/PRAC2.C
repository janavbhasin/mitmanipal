#include<stdio.h>
#include<stdlib.h>
#define size 5
typedef struct 
{
    int arr[size];
    int front,rear;
}Queue;
Queue*create_queue()
{
    Queue*queue=(Queue*)calloc(1,sizeof(Queue));
    queue->front=-1;
    queue->rear=-1;
    return queue;
}
int isempty(Queue*queue)
{
    if (queue->front==-1 && queue->rear==-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int isfull(Queue*queue)
{
    if((queue->rear + 1) % size == queue->front)
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
    if(isfull(queue)==1)
    {
        printf("the queue is full\n");
    }
    else if(isempty(queue)==1)
    {
        queue->rear=queue->front=0;
    }
    else
    {
        queue->rear = (queue->rear + 1) % size;
    }
    queue->arr[queue->rear] = item;
}
int dequeue(Queue*queue)
{
    int item;
    if(isempty(queue)==1)
    {
        printf("the queue is empty therefore cant print anything\n");
        return -1;
    }
    else 
    {
        item=queue->arr[queue->front];
        if(queue->rear==queue->front)
        {
            queue->rear=queue->front=-1;
        }
        else
        {
            queue->front = (queue->front + 1) % size;
        }
    }
    return item;
}
void display(Queue*queue)
{
    if(isempty(queue)==1)
    {
        printf("the queue is empty therefore cant print anything\n");
        return ;
    }
    else
    {
        for(int i=queue->front;i<=queue->rear;i++)
        {
            printf("%d\n",queue->arr[i]);
        }
    }
}
int main()
{
    Queue*queue=create_queue();
    int i=1;
    int item;
    while(i!=4)
    {
        printf("enter\n1 for enqueue \n2 for dequeue\n3 for display\n4 for exit\n");
        scanf("%d",&i);
        if(i==1)
        {
            printf("enter the element to be queued: ");
            scanf("%d",&item);
            enque(queue,item);
        }
        else if(i==2)
        {
            printf("dequeued %d\n",dequeue(queue));
        }
        else if(i==3)
        {
            printf("the elements of the queue are: \n");
            display(queue);
        }
        else if(i==4)
        {
            printf("bye bye\n");
            break;
        }
    }
}