#include <stdio.h>
#include <stdlib.h>
int stack[100],arr[100],k=0,top=-1;
void push(int vertex)
{
    stack[++top] = vertex;
}
int pop()
{
    return stack[top--];
}
void dfs(int mat[5][5], int visited[5], int vertices, int startvertex)
{
    push(startvertex);
    visited[startvertex] = 1;
    while (top != -1)
    {
        int currentVertex = pop();
        arr[k]=currentVertex;
        k++;
        int smallestvertex = -1;
        for (int i = 0; i < vertices; i++)
        {
            if (mat[currentVertex][i] == 1 && visited[i] != 1)
            {
                if (smallestvertex == -1 || i < smallestvertex)
                {
                    smallestvertex = i;
                }
            }
        }
        if (smallestvertex != -1)
        {
            push(smallestvertex);
            visited[smallestvertex] = 1;
        }
    }
}
int main() {
    int vertices = 5, startVertex = 0;
    int graph[5][5] = { {0, 1, 0, 1, 0}, 
    					{0, 0, 0, 1, 1}, 
    					{0, 0, 0, 0, 0}, 
    					{0, 0, 0, 0, 1}, 
    					{0, 0, 1, 0, 0}};
    int visited[5] = {0};
    dfs(graph, visited, vertices, startVertex);
    printf("\ntopological order:");
    for(int i=0;i<k;i++)
    {
    	printf("%d",arr[i]);
    }
}