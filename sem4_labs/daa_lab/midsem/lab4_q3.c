#include<stdio.h>
#include<stdlib.h>
int queue[100];
int f=-1,r=-1;
void enqueue(int x)
{
    if(f==-1)
    {
        f=0;
    }
    queue[++r]=x;
}
int dequeue()
{
    int item=queue[f++];
    if(f>r)
    {
        f=r=-1;
    }
    return item;
}
int isQueueEmpty() 
{
    return f == -1;
}
int size;
void bfs(int arr[size][size],int visited[size],int startVertex)
{
    visited[startVertex]=1;
    enqueue(startVertex);
    while(!isQueueEmpty())
    {
        int cv=dequeue();
        printf("%d\t",cv);
        for(int i=0;i<size;i++)      
	 {
            if(arr[cv][i] == 1 && visited[i] != 1)
            {
                enqueue(i);
                visited[i]=1;
            }
        }
    }
}
int main() 
{
    int  startVertex = 0, graph[5][5] = {{0, 1, 0, 1, 0},{0, 0, 1, 0, 1},{1, 0, 0, 0, 0},{0, 0, 0, 0, 1},{0, 0, 0, 0, 0}}, visited[5] = {0};
    size=5;
    bfs(graph, visited, startVertex);
}
