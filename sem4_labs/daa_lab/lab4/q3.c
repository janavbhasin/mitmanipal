#include <stdio.h>
#include <stdlib.h>
int queue[100];
int front = -1, rear = -1;
void enqueue(int vertex) 
{ 
    if (rear == 100 - 1) 
    {
        printf("Queue overflow\n");
    } 
    else 
    {   
        if (front == -1) 
        {
            front = 0;
        }
        queue[++rear] = vertex;
    }
}
int dequeue() 
{
    if (front == -1) 
    {
        printf("Queue underflow\n");
        return -1;
    } 
    else 
    {
        int item = queue[front++];
        if (front > rear) 
        {
            front = rear = -1;
        }
        return item;
    }
}
int isQueueEmpty() 
{
    return front == -1;
}
int findSmallestNeighbor(int mat[5][5], int currentVertex, int visited[5], int vertices) 
{
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
    return smallestNeighbor;
}
void bfs(int mat[5][5], int visited[5], int vertices, int startVertex) 
{
    enqueue(startVertex);
    visited[startVertex] = 1;
    while (!isQueueEmpty()) 
    {
        int currentVertex = dequeue();
        printf("Visited %d\n", currentVertex);
        int smallestNeighbor;
        while ((smallestNeighbor = findSmallestNeighbor(mat, currentVertex, visited, vertices)) != -1) 
        {
            enqueue(smallestNeighbor);
            visited[smallestNeighbor] = 1;
        }
    }
}
int main() 
{
    int vertices = 5, startVertex = 0, graph[5][5] = {{0, 1, 0, 1, 0},{0, 0, 1, 0, 1},{1, 0, 0, 0, 0},{0, 0, 0, 0, 1},{0, 0, 0, 0, 0}}, visited[5] = {0};
    bfs(graph, visited, vertices, startVertex);
}