#include<stdio.h>
#include<stdlib.h>
int queue[100];
int f=-1,r=-1;
void enqueue(int value)
{
    if(r==100-1)
    {
        return;
    }
    else
    {
        if(r==-1)
        {
            f=0;
        }
        queue[++r]=value;
    }
}
int dequeue()
{
    if(f==-1)
    {
        return -1;
    }
    else
    {
        int value=queue[f++];
        if(f>r)
        {
            f=-1;
            r=-1;
        }
        return value;
    }
}
int isQueueEmpty()
{
    if(f==-1)
    {
        return 1;
    }
    return 0;
}
int smallest(int mat[5][5],int visited[5],int currentVertex,int vertices)
{
    int small=-1;
    for(int i=0;i<vertices;i++)
    {
        if(mat[currentVertex][i]==1 && visited[i]!=1)
        {
            if(small==-1 || small>i)
            {
                small=i;
            }
        }
    }
    return small;
}
void bfs(int mat[5][5],int visited[5],int vertices,int startVertex)
{
    enqueue(startVertex);
    visited[startVertex]=1;
    while(isQueueEmpty()!=1)
    {
        int currentVertex=dequeue();
        printf("%d  ",currentVertex);
        int small;
        while((small=smallest(mat,visited,currentVertex,vertices))!=-1)
        {
            enqueue(small);
            visited[small]=1;
        }
    }
}
int main() 
{
    int vertices = 5, startVertex = 0, graph[5][5] = {{0, 1, 0, 1, 0},{0, 0, 1, 0, 1},{1, 0, 0, 0, 0},{0, 0, 0, 0, 1},{0, 0, 0, 0, 0}}, visited[5] = {0};
    bfs(graph, visited, vertices, startVertex);
}