#include <stdio.h>
#include <stdlib.h>
void topologicalSort(int graph[7][7],int vertices)
{
    int flag=0, arr[vertices],removed[vertices],k=0;
    for(int i=0;i<vertices;i++)
    {
        removed[i]=0;
    }
    while(flag!=vertices)
    {
        for(int i=0;i<vertices;i++)
        {
            arr[i]=0;
            for(int j=0;j<vertices;j++)
            {
                arr[i]=arr[i]+graph[j][i];
            }
        }
        for(int i=0;i<vertices;i++)
        {
            if(arr[i]==0 && removed[i]!=-1)
            {
                removed[i]=-1;
                printf("%d",i);
                k=i;
                break;
            }
        }
        for (int i = 0; i < vertices; i++) 
        {
            graph[k][i] = 0;
        }
        flag++;
    }
}
int main() 
{
    int vertices = 7;
    int graph[7][7] = {{0, 1, 1, 0, 0, 0, 0},{0, 0, 0, 0, 1, 0, 1}, {0, 0, 0, 0, 0, 1, 0}, {1, 1, 1, 0, 0, 1, 1},{0, 0, 0, 0, 0, 0, 0},{0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 1, 1, 0}};
    printf("Topological Sorting Order: ");
    topologicalSort(graph, vertices);
}