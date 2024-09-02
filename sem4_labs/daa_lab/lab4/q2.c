#include <stdio.h>
#include <stdlib.h>
int stack[100];
int top = -1;
void push(int vertex)
{
    stack[++top] = vertex;
}
int pop()
{
    return stack[top--];
}
int isStackEmpty()
{
    if(top==-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void dfs(int mat[4][4], int visited[4], int vertices, int startvertex)
{
    push(startvertex);
    visited[startvertex] = 1;
    while (top != -1)
    {
        int currentVertex = pop();
        printf("popped %d \n", currentVertex);
        int smallestNeighbor = -1;
        for (int i = 0; i < vertices; i++)
        {
            if (mat[currentVertex][i] == 1 && visited[i] != 1)
            {
                if (smallestNeighbor == -1 || i < smallestNeighbor)
                {
                    smallestNeighbor = i;
                }
            }
        }
        if (smallestNeighbor != -1)
        {
            push(smallestNeighbor);
            printf("pushed %d\n",smallestNeighbor);
            visited[smallestNeighbor] = 1;
        }
    }
}
int main()
{
    int vertices=4,startVertex=0,graph[4][4]={{0,1,1,1},{0,0,0,1},{0,0,0,0},{0,0,1,0}},visited[4] = {0};
    dfs(graph, visited, vertices, startVertex);
}