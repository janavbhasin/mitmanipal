#include<stdio.h>
#include<stdlib.h>
int stack[100];
int top=-1;
void push(int x)
{
    stack[++top]=x;
}
int pop()
{
    return stack[top--];
}
int size;
void dfs(int arr[size][size],int visited[size],int startVertex)
{
    push(startVertex);
    visited[startVertex]=1;
    while(top!=-1)
    {
        int cv=pop();
        printf("%d\t",cv);
        int smallestNeighbor=-1;
        for(int i=0;i<size;i++)
        {
            if(visited[i]!=1&&arr[cv][i]==1)
            {
                smallestNeighbor=i;
                break;
            }
        }
        if(smallestNeighbor!=-1)
        {
            push(smallestNeighbor);
            visited[smallestNeighbor]=1;
        }
    }
}
int main()
{
    int startVertex=0,graph[4][4]={{0,1,1,1},{0,0,0,1},{0,0,0,0},{0,0,1,0}},visited[4] = {0};
    size =4;
    dfs(graph, visited, startVertex);
}